import os
from .common import *

DEBUG = True

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

MEDIA_ROOT = os.path.join(DATA_DIR, 'media_root')
STATIC_ROOT = os.path.join(DATA_DIR, 'static_root')
