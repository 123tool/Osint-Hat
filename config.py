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

# API Config
GOOGLE_API_KEY = ""
GOOGLE_CSE_ID = ""

# Signature platform
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
    },
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
    },
    "Bitbucket": {
        "url": "https://bitbucket.org/{}/",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Development"
    },
    "DockerHub": {
        "url": "https://hub.docker.com/u/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Development"
    },
    "StackOverflow": {
        "url": "https://stackoverflow.com/users/story/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Development"
    },
    "NPM": {
        "url": "https://www.npmjs.com/~{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Development"
    },
    "Kaggle": {
        "url": "https://www.kaggle.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Data Science"
    },
    "Reddit": {
        "url": "https://www.reddit.com/user/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Social"
    },
    "Tumblr": {
        "url": "https://{}.tumblr.com",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Social"
    },
    "Flickr": {
        "url": "https://www.flickr.com/photos/{}/",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Social"
    },
    "Snapchat": {
        "url": "https://www.snapchat.com/add/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Social"
    },
    "Behance": {
        "url": "https://www.behance.net/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Design"
    },
    "Dribbble": {
        "url": "https://dribbble.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Design"
    },
    "Linktree": {
        "url": "https://linktr.ee/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Professional"
    },
    "Gumroad": {
        "url": "https://{}.gumroad.com",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Business"
    },
    "Patreon": {
        "url": "https://www.patreon.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Content Creator"
    },
    "Saweria": {
        "url": "https://saweria.co/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Indo Tech / Donation"
    },
    "Trakteer": {
        "url": "https://trakteer.id/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Indo Tech / Donation"
    },
    "Tokopedia": {
        "url": "https://www.tokopedia.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Indo E-Commerce",
        "requires_browser": True
    },
    "Bukalapak": {
        "url": "https://www.bukalapak.com/u/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Indo E-Commerce"
    },
    "Kaskus": {
        "url": "https://www.kaskus.co.id/@{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Indo Forum"
    },
    "Kompasiana": {
        "url": "https://www.kompasiana.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Indo Blogging"
    },
    "Karyakarsa": {
        "url": "https://karyakarsa.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Indo Content Creator"
    },
    "Steam": {
        "url": "https://steamcommunity.com/id/{}",
        "error_type": "message",
        "error_msg": "The specified profile could not be found",
        "category": "Gaming"
    },
    "Twitch": {
        "url": "https://www.twitch.tv/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Gaming"
    },
    "Roblox": {
        "url": "https://www.roblox.com/user.aspx?username={}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Gaming"
    },
    "Xbox_Gamertag": {
        "url": "https://account.xbox.com/en-us/profile?gamertag={}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Gaming"
    },
    "Spotify": {
        "url": "https://open.spotify.com/user/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Entertainment"
    },
    "SoundCloud": {
        "url": "https://soundcloud.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Entertainment"
    },
    "Bandcamp": {
        "url": "https://bandcamp.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Entertainment"
    },
    "Discord_Invite": {
        "url": "https://discord.gg/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Chat"
    },
    "Telegram": {
        "url": "https://t.me/{}",
        "error_type": "message",
        "error_msg": "If you have Telegram, you can contact",
        "category": "Chat"
    },
    "Quora": {
        "url": "https://www.quora.com/profile/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Forum"
    },
    "Medium": {
        "url": "https://medium.com/@{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Blogging"
    },
    "Scribd": {
        "url": "https://www.scribd.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Documents"
    },
    "SlideShare": {
        "url": "https://www.slideshare.net/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Documents"
    },
    "DailyMotion": {
        "url": "https://www.dailymotion.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Video"
    },
    "Vimeo": {
        "url": "https://vimeo.com/{}",
        "error_type": "status_code",
        "error_code": 404,
        "category": "Video"
    }
}

DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
