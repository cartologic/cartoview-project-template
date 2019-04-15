from .settings import *
import os
import sys
ROOT_URLCONF = os.getenv("ROOT_URLCONF", "{{project_name}}.urls")
WAGTAIL_SITE_NAME = "Cartoview"
APPS_DIR = os.path.join(BASE_DIR, os.pardir, "cartoview_apps")
# NOTE: load cartoview apps
if APPS_DIR not in sys.path:
    sys.path.append(APPS_DIR)
from cartoview.app_manager.config import CartoviewApp  # noqa
CartoviewApp.load(apps_dir=APPS_DIR)
for app in CartoviewApp.objects.get_active_apps().values():
    try:
        # ensure that the folder is python module
        app_module = __import__(app.name)
        app_dir = os.path.dirname(app_module.__file__)
        app_settings_file = os.path.join(app_dir, "settings.py")
        libs_dir = os.path.join(app_dir, "libs")
        if os.path.exists(app_settings_file):
            app_settings_file = os.path.realpath(app_settings_file)
            exec(open(app_settings_file).read())
        if os.path.exists(libs_dir) and libs_dir not in sys.path:
            sys.path.append(libs_dir)
        if app.name not in INSTALLED_APPS:
            INSTALLED_APPS += (app.name.__str__(), )
    except Exception as e:
        logger.error(str(e))
