## OsintHat - The Osint Hunter

**OsintHat** adalah alat investigasi Open Source Intelligence (OSINT) mutakhir yang dirancang untuk melacak dan mengungkap jejak digital subjek target di platform global dan nasional. Dengan mengombinasikan multi-threading berkecepatan tinggi, otomatisasi browser untuk bypass proteksi JavaScript, rotasi sirkuit proxy Tor, serta teknik Advanced Google Dorking, OsintHat menjadi senjata andalan para investigator siber, analis intelijen, dan pentester.

---

## ⚡ Fitur
*   **Pengecekan Profil Langsung:** Verifikasi instan ketersediaan nama pengguna (username) di ribuan platform secara simultan.
*   **Rotasi Proxy Tor:** Pengalihan lalu lintas data otomatis via jaringan Tor untuk menghindari pemblokiran IP (*rate-limiting*) dan menjaga anonimitas operasi.
*   **Mode Browser (Selenium):** Kemampuan merender halaman web modern berbasis JavaScript/SPA guna mengelabui sistem proteksi anti-bot.
*   **Advanced Dorking Engine:** Generator kueri mesin pencari otomatis untuk memburu dokumen publik sensitif (`filetype:pdf`, `site:`, dll.).
*   **Deep Extraction:** Pembedahan konten HTML menggunakan ekspresi reguler (Regex) untuk menarik data email, nomor telepon, bio, dan dokumen terkait.
*   **Penilaian Kepercayaan (Trust Score):** Algoritma penilaian (0–100%) untuk menyaring hasil palsu (*false-positives*) berdasarkan validasi silang metadata.
*   **Graceful Partial Save:** Mekanisme penyelamatan data otomatis. Jika Anda menekan `Ctrl+C` di tengah proses, progres pemindaian yang sudah berjalan tidak akan hilang dan langsung diekspor menjadi laporan.

---

## 📋 Persyaratan
OsintHat dapat berjalan di berbagai sistem operasi dengan dependensi berikut:

| Sistem Operasi | Status | Catatan |
| :--- | :--- | :--- |
| **Kali Linux / Parrot OS** | ✅ Teruji Penuh | Python 3, Chromium, dan layanan Tor sudah terpasang bawaan. |
| **Ubuntu / Debian** | ✅ Berhasil | Perlu memasang Python 3.7+, `pip`, `tor`, dan paket `chromium-driver`. |
| **macOS** | ✅ Berhasil | Membutuhkan Python 3.7+ via Homebrew; instal Chrome/Chromium secara terpisah. |
| **Windows** | ✅ Berhasil | Membutuhkan Python 3.7+ dan Google Chrome. Fitur Tor bersifat opsional. |

---
## 🚀 Instalasi
Ikuti langkah-langkah berikut untuk memasang OsintHat di perangkat Anda :

## 1. Kloning Repositori & Direktori
```bash
git clone https://github.com/123tool/Osint-Hat.git
cd Osint-Hat
```
## 2. Dependensi Python
​Pasang seluruh pustaka pihak ketiga yang dibutuhkan menggunakan pip :
```
pip install -r requirements.txt
```
(Atau pasang manual jika tidak menggunakan file requirements.txt :
```
pip install requests beautifulsoup4 selenium stem pysocks
```
## 3. Konfigurasi Layanan Tor
​Jika Anda ingin menggunakan fitur rotasi IP (--tor), pastikan layanan Tor di sistem operasi Anda sudah aktif :

- ​**Linux :**
```
    sudo systemctl start tor
```
- **macOS :**
```bash
    brew services start tor
```

---

## 📖 Perintah & Penggunaan
Jalankan skrip utama menggunakan Python dengan berbagai argumen taktis sesuai kebutuhan investigasi Anda :

## 1. Pemindaian Standar (Cepat & Ringan)
Memeriksa username target di seluruh platform menggunakan request HTTP biasa tanpa proxy.
```bash
python osinthat.py --target "username_target"
```
## 2. Pemindaian Anonim (Rotasi Proxy Tor)
​Mengaktifkan jaringan Tor untuk menyamarkan alamat IP asli Anda dan memutar sirkuit secara berkala.
```
python osinthat.py --target "username_target" --tor
```
## 3. Mode Browser Agresif
​Menggunakan Selenium Headless Browser untuk memuat situs web berat yang memproteksi datanya di balik render JavaScript.
```
python osinthat.py --target "username_target" --browser --threads 10
```
## 4. Investigasi Intelijen
​Mengombinasikan rotasi Tor, otomatisasi browser, pencarian dokumen lewat Google Dorking, serta menyimpan hasil ke file laporan kustom.
```
python osinthat.py --target "target_operasi" --tor --browser --dork --output laporan_intel_final
```

## Disclaimer

​Alat ini dibuat murni untuk tujuan edukasi, pengujian keamanan sah, investigasi jurnalistik, dan forensik digital. Penyalahgunaan alat ini untuk aktivitas ilegal, penguntitan (stalking), atau pelanggaran privasi orang lain di luar hukum yang berlaku sepenuhnya merupakan tanggung jawab pengguna masing-masing.
