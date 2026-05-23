import urllib.parse
from bs4 import BeautifulSoup
import json
from config import GOOGLE_API_KEY, GOOGLE_CO_ID, GOOGLE_CSE_ID

class GoogleSearchEngine:
    def __init__(self, request_handler):
        self.rh = request_handler # Menggunakan session tor_proxy

    def dork_search_scraper(self, query, pages=2):
        """Scraping manual Google Dorking gratis tanpa API Key"""
        results = []
        for page in range(0, pages * 10, 10):
            url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&start={page}"
            try:
                response = self.rh.get(url)
                if response.status_code == 429:
                    # Terdeteksi rate-limit, otomatis rotasi IP jika Tor aktif
                    if self.rh.rotate_ip():
                        response = self.rh.get(url)
                    else:
                        break # Stop jika diblokir keras
                
                soup = BeautifulSoup(response.text, "html.parser")
                # Menangkap selector blok pencarian Google standar
                for g in soup.find_all('div', class_='g'):
                    anchors = g.find_all('a')
                    if anchors:
                        link = anchors[0]['href']
                        title = g.find('h3').text if g.find('h3') else link
                        if link.startswith("http"):
                            results.append({"title": title, "url": link})
            except Exception:
                pass
        return results

    def search_via_api(self, query):
        """Pencarian Google menggunakan Custom Search API Resmi"""
        if not GOOGLE_API_KEY or not GOOGLE_CSE_ID:
            # Fallback otomatis ke mode scraper jika API keys kosong
            return self.dork_search_scraper(query)
            
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": GOOGLE_API_KEY,
            "cx": GOOGLE_CSE_ID,
            "q": query
        }
        
        try:
            res = self.rh.get(url, params=params)
            if res.status_code == 200:
                data = res.json()
                items = data.get("items", [])
                return [{"title": i.get("title"), "url": i.get("link")} for i in items]
        except Exception:
            pass
        return []

    def execute_dorks(self, target_name, filetype=None, site=None):
        """Fungsi builder otomatisasi Dorking Tingkat Lanjut"""
        dork_query = f'"{target_name}"'
        if filetype:
            dork_query += f" filetype:{filetype}"
        if site:
            dork_query += f" site:{site}"
            
        return self.search_via_api(dork_query)
