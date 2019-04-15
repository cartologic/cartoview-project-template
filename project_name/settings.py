# -*- coding: utf-8 -*-
import os
from cartoview.settings.base import *

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)
# static settings section
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, os.pardir, "static_root")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATICFILES_DIRS = []
ROOT_URLCONF = os.getenv("ROOT_URLCONF", "{{project_name}}.urls")
APPS_DIR = os.path.abspath(os.path.join(BASE_DIR, "apps"))
try:
    from .local_settings import *
except ImportError:
    pass
