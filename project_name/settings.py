try:
    from pre_settings import *
except:
    pass
import os
import cartoview
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cartoview_settings_path = os.path.join(os.path.dirname(cartoview.__file__), 'settings.py')
execfile(cartoview_settings_path)

try:
    from local_settings import *
except:
    pass

OGC_SERVER['default']['LOCATION'] = GEOSERVER_LOCATION
OGC_SERVER['default']['PUBLIC_LOCATION'] = GEOSERVER_PUBLIC_LOCATION
OGC_SERVER['default']['LOG_FILE'] = os.path.join(BASE_DIR, "geoserver.log")
if 'datastore' in DATABASES:
  OGC_SERVER['default']['DATASTORE'] = 'datastore'

MIDDLEWARE_CLASSES += ( "django.middleware.gzip.GZipMiddleware",)

if 'geonode.geoserver' in INSTALLED_APPS and "LOCAL_GEOSERVER" in locals() and LOCAL_GEOSERVER in MAP_BASELAYERS:
       LOCAL_GEOSERVER["source"]["url"] = OGC_SERVER['default']['PUBLIC_LOCATION'] + "wms"

ALLOWED_HOSTS =['*']
