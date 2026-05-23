import requests
import time
from config import DEFAULT_USER_AGENT

class TorManager:
    def __init__(self, tor_port=9050, control_port=9051, password=None):
        self.tor_port = tor_port
        self.control_port = control_port
        self.password = password
        self.enabled = False
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": DEFAULT_USER_AGENT})

    def enable_tor(self):
        """Mengaktifkan routing proxy SOCKS5 via Tor"""
        proxies = {
            'http': f'socks5h://127.0.0.1:{self.tor_port}',
            'https': f'socks5h://127.0.0.1:{self.tor_port}'
        }
        self.session.proxies.update(proxies)
        self.enabled = True
        try:
            my_ip = self.session.get("https://api.ipify.org", timeout=10).text
            return True, my_ip
        except Exception as e:
            self.enabled = False
            self.session.proxies.clear()
            return False, str(e)

    def rotate_ip(self):
        """Meminta sirkuit IP baru ke service Tor menggunakan Control Port"""
        if not self.enabled:
            return False
        
        try:
            from stem import Signal
            from stem.control import Controller
            
            with Controller.from_port(port=self.control_port) as controller:
                if self.password:
                    controller.authenticate(password=self.password)
                else:
                    controller.authenticate()  # Mencoba tanpa password
                
                controller.signal(Signal.NEWNYM)
                time.sleep(2) # Beri jeda sirkuit Tor untuk berganti
                return True
        except ImportError:
            # Fallback jika library 'stem' tidak dipasang, abaikan rotasi kontrol keras
            return False
        except Exception:
            return False

    def get(self, url, **kwargs):
        """Wrapper request GET aman"""
        if "timeout" not in kwargs:
            kwargs["timeout"] = 15
        return self.session.get(url, **kwargs)
