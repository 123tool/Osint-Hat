import concurrent.futures
from config import PLATFORMS

class ProfileChecker:
    def __init__(self, request_handler, browser_engine=None):
        self.rh = request_handler
        self.browser = browser_engine

    def check_single_platform(self, platform_name, username):
        """Memeriksa satu platform spesifik apakah username tersedia"""
        details = PLATFORMS.get(platform_name)
        if not details:
            return None

        target_url = details["url"].format(username)
        result = {
            "platform": platform_name,
            "url": target_url,
            "status": "Tidak Ditemukan",
            "category": details.get("category", "General"),
            "method": "HTTP Request"
        }

        try:
            # Gunakan browser jika proteksi JavaScript ketat, default pakai request biasa
            if details.get("requires_browser") and self.browser:
                result["method"] = "Browser Automation"
                html_source = self.browser.fetch_page_source(target_url)
                if html_source and details["error_msg"] not in html_source:
                    result["status"] = "Ditemukan"
            else:
                response = self.rh.get(target_url, allow_redirects=True)
                
                if details["error_type"] == "status_code":
                    if response.status_code != details["error_code"]:
                        result["status"] = "Ditemukan"
                elif details["error_type"] == "message":
                    if details["error_msg"] not in response.text:
                        result["status"] = "Ditemukan"
                        
        except Exception:
            result["status"] = "Error / Terblokir"

        return result

    def scan_username(self, username, max_threads=20, progress_callback=None):
        """Engine utama untuk memicu thread paralel ke seluruh platform"""
        found_profiles = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = {
                executor.submit(self.check_single_platform, name, username): name 
                for name in PLATFORMS.keys()
            }
            
            for future in concurrent.futures.as_completed(futures):
                res = future.result()
                if res:
                    if progress_callback:
                        progress_callback(res)
                    if res["status"] == "Ditemukan":
                        found_profiles.append(res)
                        
        return found_profiles
