import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class BrowserEngine:
    def __init__(self, headless=True, tor_proxy=None):
        self.headless = headless
        self.tor_proxy = tor_proxy
        self.driver = None

    def init_driver(self):
        """Inisialisasi Selenium Driver dengan argumen anti-deteksi"""
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless=new")
        
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("window-size=1280,800")
        chrome_options.add_argument("--log-level=3")
        
        if self.tor_proxy:
            # Format proxy untuk selenium bypass socks
            chrome_options.add_argument(f'--proxy-server=socks5://127.0.0.1:{self.tor_proxy}')

        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            # Script injeksi untuk menyembunyikan sidik jari automation selenium
            self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
            })
        except Exception as e:
            raise RuntimeError(f"Gagal memuat WebDriver Browser Engine: {str(e)}")

    def fetch_page_source(self, url):
        """Mengambil data html halaman setelah dirender sempurna"""
        if not self.driver:
            self.init_driver()
        try:
            self.driver.get(url)
            # Menunggu payload DOM selesai (bisa ditambah WebDriverWait secara situasional)
            return self.driver.page_source
        except Exception:
            return ""

    def close(self):
        if self.driver:
            self.driver.quit()
