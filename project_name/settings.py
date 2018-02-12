# -*- coding: utf-8 -*-
try:
    from pre_settings import *
except:
    pass
import os
import cartoview


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)
cartoview_settings_path = os.path.join(
    os.path.dirname(cartoview.__file__), 'settings.py')
execfile(cartoview_settings_path)
# bower static files
STATICFILES_DIRS += [os.path.join(PROJECT_DIR, "static"), ]
# django Media Section
# uncomment the following if you want your files out of geonode folder
MEDIA_ROOT = os.path.join(BASE_DIR, "uploaded")
MEDIA_URL = "/uploaded/"
LOCAL_MEDIA_URL = "/uploaded/"
# static section
STATIC_ROOT = os.path.join(BASE_DIR, "static")
try:
    from local_settings import *
except:
    pass

if 'datastore' in DATABASES:
    OGC_SERVER['default']['DATASTORE'] = 'datastore'

MIDDLEWARE_CLASSES += ("django.middleware.gzip.GZipMiddleware",)

if 'geonode.geoserver' in INSTALLED_APPS and "LOCAL_GEOSERVER" in locals() and LOCAL_GEOSERVER in MAP_BASELAYERS:
    LOCAL_GEOSERVER["source"]["url"] = OGC_SERVER['default']['PUBLIC_LOCATION'] + "wms"
