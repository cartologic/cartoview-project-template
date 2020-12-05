# -*- coding: utf-8 -*-
import os
from cartoview.settings import *
# django project name
PROJECT_NAME = "{{project_name}}"
# web site human readable name
SITE_NAME = os.getenv("SITE_NAME", PROJECT_NAME)
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
except Exception as e:
    print('error while importing local settings: ', e)

# cartoview setings
TEMPLATES[0]["DIRS"] = CARTOVIEW_TEMPLATE_DIRS + TEMPLATES[0]["DIRS"]
from cartoview import app_manager
from past.builtins import execfile
app_manager_settings = os.path.join(
    os.path.dirname(app_manager.__file__), "settings.py")
execfile(os.path.realpath(app_manager_settings))
load_apps(APPS_DIR)
INSTALLED_APPS += CARTOVIEW_APPS

# adding current project to installed apps
INSTALLED_APPS += (PROJECT_NAME,)

# using project templates if cartoview_cms is installed
if "cartoview_cms" in INSTALLED_APPS:
    currrent_templates_dirs = [os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'templates'
    )]
    TEMPLATES[0]["DIRS"] = currrent_templates_dirs + TEMPLATES[0]["DIRS"]


# adding cartoview apps settings files 
for settings_file in APPS_SETTINGS:
    try:
        execfile(settings_file)
    except Exception as e:
        print(e.message)
