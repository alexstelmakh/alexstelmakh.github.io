import time


LOAD_CONTENT_CACHE = False
FILENAME_METADATA = '(?P<title>.*)'
ARTICLE_PATHS = ['articles/web_development']
PAGE_PATHS = ['pages']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
DEFAULT_DATE_FORMAT = "%d/%m/%Y"
DEFAULT_DATE = (time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday)
SITESUBTITLE = ""
TAG_URL = 'tags/{slug}'
TAG_SAVE_AS = 'tags/{slug}.html'
CATEGORY_URL = 'category/{slug}'
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = ARCHIVES_URL + "index.html"
INDEX_URL = ''
USE_FOLDER_AS_CATEGORY = True
ARTICLE_ORDER_BY = 'reversed-date'

TWITTER_USERNAME = 'AlexStelmakh'

CONTACTS = [
    ("GitHub", "github", "https://github.com/alexstelmakh"),
    ("LinkedIn", "linkedin-in", "https://www.linkedin.com/in/alex-stelmakh-204b66112/"),
    ("Twitter", "twitter", "http://twitter.com/alexstelmakh"),
    ("Telegram", "paper-plane", "https://t.me/This_is_111e")
]

AUTHOR = 'Alex Stelmakh'
SITENAME = "Alex Stelmakh's blog"
SITEURL = ''

PATH = 'content'
THEME = "theme"
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {"extra/favicon.ico": {"path": "favicon.ico"}}
THEME_STATIC_PATHS = ['static']

TIMEZONE = 'Europe/Kiev'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
AUTHOR_SAVE_AS = ''

# Social widget
SOCIAL = [
    {"name": "GitHub", "icon": "github", "url": "https://github.com/alexstelmakh"},
    {"name": "LinkedIn", "icon": "linkedin-in", "url": "https://www.linkedin.com/in/alex-stelmakh/"}
]

RELATED_POSTS_MAX = 10
DEFAULT_PAGINATION = 10
DEFAULT_LANG = 'en'
