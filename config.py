import sys

VERSION = "1.0.0"
BANNER = f"""
  ____       _           _   _   _       _   
 / __ \     (_)         | | | | | |     | |  
| |  | | ___ _ _ __  ___| |_| |_| | __ _| |_ 
| |  | |/ __| | '_ \/ __| __|  _  |/ _` | __|
| |__| |\__ \ | | | \__ \ |_| | | | (_| | |_ 
 \____/ |___/_|_| |_|___/\__\_| |_|\__,_|\__| v{VERSION}
      [ The Ultimate Digital Footprint Hunter ]
"""

# Default API Config (Google Custom Search Engine)
GOOGLE_API_KEY = ""
GOOGLE_CSE_ID = ""

# Signature platform (Dapat diperluas menggunakan list json / sherlock database)
PLATFORMS = {
    "GitHub": {
        "url": "https://github.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Development"
    },
    "Twitter": {
        "url": "https://x.com/{}",
        "error_type": "message",
        "error_msg": "This account doesn’t exist",
        "category": "Social"
    },
    "Instagram": {
        "url": "https://www.instagram.com/{}/",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Social"
    },
    "Facebook": {
        "url": "https://www.facebook.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Social"
    },
    "LinkedIn": {
        "url": "https://www.linkedin.com/in/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Professional"
    },
    "Pinterest": {
        "url": "https://www.pinterest.com/{}/",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Social"
    },
    "TikTok": {
        "url": "https://www.tiktok.com/@{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Social"
    }
    "GitHub": {
        "url": "https://github.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Development"
    },
    "Twitter": {
        "url": "https://x.com/{}",
        "error_type": "message",
        "error_msg": "This account doesn’t exist",
        "category": "Social"
    },
    # === TAMBAHKAN PLATFORM BARU KAMU DI BAWAH INI ===
    "GitLab": {
        "url": "https://gitlab.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Development"
    },
    "SitusForumIndo": {
        "url": "https://forumindonesia.xyz/user/{}",
        "error_type": "message",
        "error_msg": "Pengguna tidak ditemukan",
        "category": "Forum"
    }
}

DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
