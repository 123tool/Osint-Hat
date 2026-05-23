class TrustScorer:
    @staticmethod
    def calculate(profile_data, metadata_extracted):
        """
        Menghitung persentase keandalan target (0 - 100%)
        Sistem pembobotan:
        - Profil Merespon HTTP 200 OK = Basis 40%
        - Memiliki deskripsi Bio/Karakteristik = +20%
        - Ditemukan metadata kontak (Email/No Telp) = +25%
        - Memiliki struktur nama pengguna identik = +15%
        """
        score = 0
        if profile_data.get("status") == "Ditemukan":
            score += 40
            
        if metadata_extracted.get("bio"):
            score += 20
            
        if metadata_extracted.get("emails") or metadata_extracted.get("phones"):
            score += 25
            
        # Validasi string tambahan jika platform mengembalikan respons kustom
        if len(profile_data.get("platform", "")) > 1:
            score += 15

        return min(score, 100)
