# -*- coding: utf-8 -*-
try:
    from .pre_settings import *
except:
    pass
import os

from cartoview.app_manager.settings import load_apps
from cartoview.settings import *

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)
APPS_DIR = os.path.abspath(os.path.join(BASE_DIR, "apps"))
PENDING_APPS = os.path.join(APPS_DIR, "pendingOperation.yml")
TEMPLATES[0]["DIRS"] = CARTOVIEW_TEMPLATE_DIRS + TEMPLATES[0]["DIRS"]

INSTALLED_APPS += load_apps()
STATICFILES_DIRS += [os.path.join(PROJECT_DIR, "static"), ]
# django Media Section
# uncomment the following if you want your files out of geonode folder
MEDIA_ROOT = os.path.join(BASE_DIR, "uploaded")
MEDIA_URL = "/uploaded/"
LOCAL_MEDIA_URL = "/uploaded/"
# static section
STATIC_ROOT = os.path.join(BASE_DIR, "static")
try:
    from .local_settings import *
except:
    pass
