## 🪓 OsintHat - The Ultimate Digital Footprint Hunter
**OsintHat** adalah alat investigasi Open Source Intelligence (OSINT) mutakhir yang dirancang untuk melacak dan mengungkap jejak digital subjek target di lebih dari 1000++ platform global dan nasional. Dengan mengombinasikan multi-threading berkecepatan tinggi, otomatisasi browser untuk bypass proteksi JavaScript, rotasi sirkuit proxy Tor, serta teknik Advanced Google Dorking, OsintHat menjadi senjata andalan para investigator siber, analis intelijen, dan pentester.
---
## ⚡ Fitur Utama
*   **Pengecekan Profil Langsung:** Verifikasi instan ketersediaan nama pengguna (username) di ribuan platform secara simultan.
*   **Rotasi Proxy Tor:** Pengalihan lalu lintas data otomatis via jaringan Tor untuk menghindari pemblokiran IP (*rate-limiting*) dan menjaga anonimitas operasi.
*   **Mode Browser (Selenium):** Kemampuan merender halaman web modern berbasis JavaScript/SPA guna mengelabui sistem proteksi anti-bot.
*   **Advanced Dorking Engine:** Generator kueri mesin pencari otomatis untuk memburu dokumen publik sensitif (`filetype:pdf`, `site:`, dll.).
*   **Deep Extraction:** Pembedahan konten HTML menggunakan ekspresi reguler (Regex) untuk menarik data email, nomor telepon, bio, dan dokumen terkait.
*   **Penilaian Kepercayaan (Trust Score):** Algoritma penilaian (0–100%) untuk menyaring hasil palsu (*false-positives*) berdasarkan validasi silang metadata.
*   **Graceful Partial Save:** Mekanisme penyelamatan data otomatis. Jika Anda menekan `Ctrl+C` di tengah proses, progres pemindaian yang sudah berjalan tidak akan hilang dan langsung diekspor menjadi laporan.
---
## 📋 Persyaratan Sistem
OsintHat dapat berjalan di berbagai sistem operasi dengan dependensi berikut:

| Sistem Operasi | Status | Catatan |
| :--- | :--- | :--- |
| **Kali Linux / Parrot OS** | ✅ Teruji Penuh | Python 3, Chromium, dan layanan Tor sudah terpasang bawaan. |
| **Ubuntu / Debian** | ✅ Berhasil | Perlu memasang Python 3.7+, `pip`, `tor`, dan paket `chromium-driver`. |
| **macOS** | ✅ Berhasil | Membutuhkan Python 3.7+ via Homebrew; instal Chrome/Chromium secara terpisah. |
| **Windows** | ✅ Berhasil | Membutuhkan Python 3.7+ dan Google Chrome. Fitur Tor bersifat opsional. |

---
## 🚀 Panduan Instalasi
Ikuti langkah-langkah berikut untuk memasang OsintHat di perangkat Anda:
### 1. Kloning Repositori & Masuk ke Direktori
```bash
git clone [https://github.com/username-anda/osinthat.git](https://github.com/username-anda/osinthat.git)
cd osinthat
