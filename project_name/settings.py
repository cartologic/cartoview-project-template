try:
    from pre_settings import *
except:
    pass
import os
import cartoview


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)
cartoview_settings_path = os.path.join(os.path.dirname(cartoview.__file__), 'settings.py')
execfile(cartoview_settings_path)
#bower static files
STATICFILES_DIRS += [os.path.join(PROJECT_DIR, "static"),]
#django Media Section
#uncomment the following if you want your files out of geonode folder
MEDIA_ROOT = os.path.join(BASE_DIR, "uploaded")
MEDIA_URL = "/uploaded/"
LOCAL_MEDIA_URL = "/uploaded/"
#static section
STATIC_ROOT = os.path.join(BASE_DIR, "static")
ALLOWED_HOSTS =['*']
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


#uncomment the following to enable geonode client
#INSTALLED_APPS += ('geonode-client',)
#LAYER_PREVIEW_LIBRARY="react"


#uncomment the following to enable osgeo_importer
#INSTALLED_APPS += ('osgeo_importer',)
#DATABASES['datastore']= {
#        'ENGINE': 'django.contrib.gis.db.backends.postgis',
#        'NAME': 'cartoview_datastore',
#        'USER' : 'cartologic',
#        'PASSWORD' : 'root',
#        'HOST' : 'postgis',
#        'PORT' : '5432',
#}
#### osgeo_importer settings
#OSGEO_DATASTORE = 'datastore'
#OSGEO_IMPORTER_GEONODE_ENABLED = True
#OSGEO_IMPORTER_VALID_EXTENSIONS = [
#    'shp', 'shx', 'prj', 'dbf', 'kml', 'geojson', 'json', 'tif', 'tiff',
#    'gpkg', 'csv', 'zip', 'xml', 'sld'
#]
#IMPORT_HANDLERS = [
    # If GeoServer handlers are enabled, you must have an instance of geoserver running.
    # Warning: the order of the handlers here matters.
#    'osgeo_importer.handlers.FieldConverterHandler',
#    'osgeo_importer.handlers.geoserver.GeoserverPublishHandler',
#    'osgeo_importer.handlers.geoserver.GeoserverPublishCoverageHandler',
#    'osgeo_importer.handlers.geoserver.GeoServerTimeHandler',
#    'osgeo_importer.handlers.geoserver.GeoWebCacheHandler',
#    'osgeo_importer.handlers.geoserver.GeoServerBoundsHandler',
#    'osgeo_importer.handlers.geoserver.GenericSLDHandler',
#    'osgeo_importer.handlers.geonode.GeoNodePublishHandler',
#     'osgeo_importer.handlers.mapproxy.publish_handler.MapProxyGPKGTilePublishHandler',
#    'osgeo_importer.handlers.geoserver.GeoServerStyleHandler',
#    'osgeo_importer.handlers.geonode.GeoNodeMetadataHandler'
#]

#PROJECTION_DIRECTORY = os.path.join(PROJECT_ROOT, "data")

