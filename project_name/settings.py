# -*- coding: utf-8 -*-
import os
from cartoview.settings import *

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# static settings section
STATICFILES_DIRS += [os.path.join(PROJECT_DIR, "static"), ]
MEDIA_ROOT = os.path.join(BASE_DIR, "uploaded")
MEDIA_URL = "/uploaded/"
LOCAL_MEDIA_URL = "/uploaded/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
APPS_DIR = os.path.abspath(os.path.join(BASE_DIR, "apps"))
try:
    from .local_settings import *
except:
    pass

# cartoview setings
TEMPLATES[0]["DIRS"] = CARTOVIEW_TEMPLATE_DIRS + TEMPLATES[0]["DIRS"]
from cartoview import app_manager
from past.builtins import execfile
app_manager_settings = os.path.join(
    os.path.dirname(app_manager.__file__), "settings.py")
execfile(os.path.realpath(app_manager_settings))
load_apps(APPS_DIR)
INSTALLED_APPS += CARTOVIEW_APPS
for settings_file in APPS_SETTINGS:
    try:
        execfile(settings_file)
    except Exception as e:
        print(e.message)
