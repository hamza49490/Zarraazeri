import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "24066716"))
API_HASH = getenv("API_HASH", "09e30e6e0b1a4c71e43a055979c51b3b")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7607259347:AAF90Z3_RNXo0FqMuUWmulD_EuJ4vYHkNdQ")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Kingbrukh:kingkhan@kingbruh.ra3pjgm.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002028213552"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6184936428"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/hamza49490/Zarraazeri",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ZaTRaSPoRT")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TheZatraGrup")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "false"))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "false")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "AgFvOpwACWwRTc4CfSYzq2r3P0cl6kE4Xm1NgL02OU9XM2W3VxQWA_0ROUZxozfJzhyzfCA_15zBt8WhzkOOOGLCjnCtQbmMC_kAgMyHSOO-9mfZMwssO7Ni_GNusVgdUJBvczvxL3uSA-Kb33WSwfCsvulGQdCPEpspid7JFZbjCywZoyNPcsTTWeXtIOhdUbW83ZmheWulFgZpuJbEK9WoF1snLZYQTtbOio0jiSewHE1B6eOEWu0iMTaYdsXyD7fWyKoYnKgBOo-NzzvPKU9n0bAH9DoyjGLYJf0xmjtwAl_w6w6dHV0E80XzvHy9_YINjBJnGJKxv5BG1tYkFSRvIXerKQAAAAA8-neEAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/e319a310659ee07929a2a.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/e319a310659ee07929a2a.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/e319a310659ee07929a2a.jpg"
STATS_IMG_URL = "https://telegra.ph/file/e319a310659ee07929a2a.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/e319a310659ee07929a2a.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e319a310659ee07929a2a.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/e319a310659ee07929a2a.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/e319a310659ee07929a2a.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/e319a310659ee07929a2a.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/e319a310659ee07929a2a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/e319a310659ee07929a2a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/e319a310659ee07929a2a.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
