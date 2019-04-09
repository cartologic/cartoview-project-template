from cartoview.settings.base import BASE_DIR, INSTALLED_APPS, logger
import os
import sys
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<db_name>',
        'USER': '<db_user>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': '5432',
        # 'CONN_MAX_AGE': 30,
    },
}
SECRET_KEY = "c8(50gzg=^s6&m73&801%+@$24+&8duk$^^4ormfkbj!*q86fo"
OAUTH_SERVER_BASEURL = "<OAUTH_SERVER_BASEURL>"
ROOT_URLCONF = os.getenv("ROOT_URLCONF", "{{project_name}}.urls")
WAGTAIL_SITE_NAME = "Cartoview"
ALLOWED_HOSTS = ['*']
APPS_DIR = os.path.join(BASE_DIR, os.pardir, "cartoview_apps")
STAND_ALONE = True
if STAND_ALONE:

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
