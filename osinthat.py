import os
import sys
import argparse
import signal
from config import BANNER, VERSION
from core.tor_proxy import TorManager
from core.browser import BrowserEngine
from core.search import GoogleSearchEngine
from core.checker import ProfileChecker
from utils.extractor import DataExtractor
from utils.trust_score import TrustScorer
from utils.reporter import ReportManager

# Global reporter pointer untuk Ctrl+C handler
reporter = None

def graceful_exit_handler(sig, frame):
    """Interupsi Ctrl+C ditangkap di sini, progress parsial diselamatkan seketika"""
    print("\n\n[!] Proses dihentikan paksa oleh pengguna (Ctrl+C). Menyimpan data parsial...")
    if reporter:
        json_f = reporter.save_json()
        txt_f = reporter.save_txt()
        print(f"[*] Berkas laporan parsial aman disimpan di: {json_f} & {txt_f}")
    sys.exit(0)

def main():
    global reporter
    signal.signal(signal.SIGINT, graceful_exit_handler)
    
    print(BANNER)
    
    parser = argparse.ArgumentParser(description="OsintHat - Alat Investigasi Jejak Digital Termutakhir")
    parser.add_argument("-t", "--target", required=True, help="Nama pengguna (username) atau entitas target")
    parser.add_argument("--threads", type=int, default=20, help="Jumlah concurrent thread pencarian (Default: 20)")
    parser.add_argument("--tor", action="store_true", help="Aktifkan perayapan aman anonim dengan rotasi proxy Tor")
    parser.add_argument("--browser", action="store_true", help="Gunakan otomatisasi Selenium Driver (Render JavaScript)")
    parser.add_argument("--dork", action="store_true", help="Eksekusi Advanced Google Dorking otomatis")
    parser.add_argument("-o", "--output", help="Nama khusus file output dasar tanpa ekstensi")
    
    args = parser.parse_args()
    target = args.target
    
    reporter = ReportManager(target)
    extractor = DataExtractor()
    
    # 1. Inisialisasi Proxy Tor jika diinstruksikan
    tor_mgr = TorManager()
    if args.tor:
        print("[*] Mengoneksikan ke sirkuit proxy Tor lokal...")
        success, info = tor_mgr.enable_tor()
        if success:
            print(f"[+] Tor Aktif! IP Investigasi Anda Berubah -> {info}")
        else:
            print(f"[-] Gagal terhubung ke Tor Daemon: {info}. Berjalan tanpa proxy.")
            
    # 2. Inisialisasi Selenium Engine jika opsi browser diaktifkan
    browser_eng = None
    if args.browser:
        print("[*] Menyiapkan Driver Selenium Headless Browser...")
        browser_eng = BrowserEngine(headless=True, tor_proxy=9050 if args.tor else None)
        
    # 3. Eksekusi Live Platform Checking
    print(f"[*] Meluncurkan pemindaian multi-threaded pada target: {target}")
    checker = ProfileChecker(request_handler=tor_mgr, browser_engine=browser_eng)
    
    def on_find(res):
        if res["status"] == "Ditemukan":
            # Ambil HTML content halaman untuk dikuliti metadatanya
            html = ""
            if args.browser and browser_eng:
                html = browser_eng.fetch_page_source(res["url"])
            else:
                try: html = tor_mgr.get(res["url"]).text 
                except: pass
                
            meta = extractor.extract_metadata(html)
            score = TrustScorer.calculate(res, meta)
            res["trust_score"] = score
            
            # Print feedback visual instan di terminal
            print(f" [+] Ditemukan: {res['platform']} -> {res['url']} [{score}% Confidence]")
            
            reporter.add_profile(res)
            reporter.update_metadata(meta)
            
    checker.scan_username(target, max_threads=args.threads, progress_callback=on_find)
    
    # 4. Eksekusi Google Dorking Tingkat Lanjut jika diminta
    if args.dork:
        print("[*] Melakukan Advanced Google Dorking untuk dokumen publik...")
        search_eng = GoogleSearchEngine(request_handler=tor_mgr)
        dork_hits = search_eng.execute_dorks(target, filetype="pdf")
        reporter.add_search_hits(dork_hits)
        print(f"[+] Selesai! Berhasil merekam {len(dork_hits)} dokumen terkait target dari mesin pencari.")
        
    # Clean up browser
    if browser_eng:
        browser_eng.close()
        
    # 5. Compile & Tampilkan Hasil Analisis Akhir (Keluaran)
    print("\n" + "="*45)
    print("        RANGKUMAN HASIL INVESTIGASI         ")
    print("="*45)
    print(f" Total Profil Terlacak     : {len(reporter.report_data['profiles_found'])}")
    print(f" Profil Terverifikasi (>=50%): {len([p for p in reporter.report_data['profiles_found'] if p.get('trust_score', 0) >= 50])}")
    print(f" Dokumen Rahasia Ditemukan : {len(reporter.report_data['documents_uncovered'])}")
    print(f" Kontak Email Terekstrak   : {len(reporter.report_data['extracted_contacts']['emails'])}")
    print(f" Kontak Telepon Terekstrak : {len(reporter.report_data['extracted_contacts']['phones'])}")
    print("="*45)
    
    # Simpan Laporan Akhir
    out_j = reporter.save_json(f"{args.output}.json" if args.output else None)
    out_t = reporter.save_txt(f"{args.output}.txt" if args.output else None)
    print(f"[+] Laporan investigasi final sukses diekspor ke:\n -> {out_j}\n -> {out_t}")

if __name__ == "__main__":
    main()
