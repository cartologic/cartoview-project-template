# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from __future__ import print_function
from past.builtins import execfile
import os
from distutils.util import strtobool
import dj_database_url
from .settings import *
SITEURL = os.getenv("SITEURL", "http://localhost/")
DATABASE_URL = os.getenv('DATABASE_URL',
                         'sqlite:////{}/database.sqlite'.format(BASE_DIR))
DATASTORE_DATABASE_URL = os.getenv('DATASTORE_DATABASE_URL', None)
if DATABASE_URL:
    DATABASES['default'] = dj_database_url.parse(
        DATABASE_URL, conn_max_age=600)
if DATASTORE_DATABASE_URL:
    DATABASES['datastore'] = dj_database_url.parse(
        DATASTORE_DATABASE_URL, conn_max_age=600)
GEOSERVER_LOCATION = os.getenv('GEOSERVER_LOCATION',
                               'http://localhost:8080/geoserver/')

GEOSERVER_PUBLIC_LOCATION = os.getenv('GEOSERVER_PUBLIC_LOCATION',
                                      'http://localhost/geoserver/')

OGC_SERVER_DEFAULT_USER = os.getenv('GEOSERVER_ADMIN_USER', 'admin')

OGC_SERVER_DEFAULT_PASSWORD = os.getenv('GEOSERVER_ADMIN_PASSWORD',
                                        'geoserver')

GEOFENCE_SECURITY_ENABLED = True

# OGC (WMS/WFS/WCS) Server Settings
# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default': {
        'BACKEND':
        'geonode.geoserver',
        'LOCATION':
        GEOSERVER_LOCATION,
        'LOGIN_ENDPOINT':
        'j_spring_oauth2_geonode_login',
        'LOGOUT_ENDPOINT':
        'j_spring_oauth2_geonode_logout',
        # PUBLIC_LOCATION needs to be kept like this because in dev mode
        # the proxy won't work and the integration tests will fail
        # the entire block has to be overridden in the local_settings
        'PUBLIC_LOCATION':
        GEOSERVER_PUBLIC_LOCATION,
        'USER':
        OGC_SERVER_DEFAULT_USER,
        'PASSWORD':
        OGC_SERVER_DEFAULT_PASSWORD,
        'MAPFISH_PRINT_ENABLED':
        True,
        'PRINT_NG_ENABLED':
        True,
        'GEONODE_SECURITY_ENABLED':
        True,
        'GEOFENCE_SECURITY_ENABLED':
        GEOFENCE_SECURITY_ENABLED,
        'GEOFENCE_URL':
        os.getenv('GEOFENCE_URL', 'internal:/'),
        'GEOGIG_ENABLED':
        False,
        'WMST_ENABLED':
        False,
        'BACKEND_WRITE_ENABLED':
        True,
        'WPS_ENABLED':
        False,
        'LOG_FILE':
        '%s/geoserver/data/logs/geoserver.log' % os.path.abspath(
            os.path.join(BASE_DIR, os.pardir)),
        # Set to name of database in DATABASES dictionary to enable
        # 'datastore',
        'DATASTORE':
        os.getenv('DEFAULT_BACKEND_DATASTORE', ''),
        'PG_GEOGIG':
        False,
        # 'CACHE': ".cache"  # local cache file to for HTTP requests
        # number of seconds to allow for HTTP requests
        'TIMEOUT':
        int(os.getenv('OGC_REQUEST_TIMEOUT', '10'))
    }
}

# GeoNode javascript client configuration

DEFAULT_MAP_CRS = "EPSG:3857"

DEFAULT_LAYER_FORMAT = "image/png"

# Where should newly created maps be focused?
DEFAULT_MAP_CENTER = (0, 0)

# How tightly zoomed should newly created maps be?
# 0 = entire world;
# maximum zoom is between 12 and 15 (for Google Maps, coverage varies by area)
DEFAULT_MAP_ZOOM = 0

# BASE MAPS
ALT_OSM_BASEMAPS = os.environ.get('ALT_OSM_BASEMAPS', True)
CARTODB_BASEMAPS = os.environ.get('CARTODB_BASEMAPS', True)
STAMEN_BASEMAPS = os.environ.get('STAMEN_BASEMAPS', True)
THUNDERFOREST_BASEMAPS = os.environ.get('THUNDERFOREST_BASEMAPS', True)
MAPBOX_ACCESS_TOKEN = os.environ.get('MAPBOX_ACCESS_TOKEN', '<MapBox_Key>')
BING_API_KEY = os.environ.get('BING_API_KEY', '<BING_API_KEY>')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', '<GOOGLE_API_KEY>')

MAP_BASELAYERS = [
    {
        "source": {
            "ptype": "gxp_olsource"
        },
        "type": "OpenLayers.Layer",
        "args": ["No background"],
        "name": "background",
        "visibility": False,
        "fixed": True,
        "group": "background"
    },
    # {
    #     "source": {"ptype": "gxp_olsource"},
    #     "type": "OpenLayers.Layer.XYZ",
    #     "title": "TEST TILE",
    #     "args": ["TEST_TILE", "http://test_tiles/tiles/${z}/${x}/${y}.png"],
    #     "name": "background",
    #     "attribution": "&copy; TEST TILE",
    #     "visibility": False,
    #     "fixed": True,
    #     "group":"background"
    # },
    {
        "source": {
            "ptype": "gxp_osmsource"
        },
        "type": "OpenLayers.Layer.OSM",
        "name": "mapnik",
        "visibility": True,
        "fixed": True,
        "group": "background"
    }
]

if 'geonode.geoserver' in INSTALLED_APPS:
    LOCAL_GEOSERVER = {
        "source": {
            "ptype": "gxp_wmscsource",
            "url": OGC_SERVER['default']['PUBLIC_LOCATION'] + "wms",
            "restUrl": "/gs/rest"
        }
    }
    baselayers = MAP_BASELAYERS
    MAP_BASELAYERS = [LOCAL_GEOSERVER]
    MAP_BASELAYERS.extend(baselayers)

# Define email service on GeoNode
EMAIL_ENABLE = strtobool(os.getenv('EMAIL_ENABLE', 'False'))

if EMAIL_ENABLE:
    EMAIL_BACKEND = os.getenv(
        'DJANGO_EMAIL_BACKEND',
        default='django.core.mail.backends.smtp.EmailBackend')
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = 'GeoNode <no-reply@geonode.org>'
else:
    EMAIL_BACKEND = os.getenv(
        'DJANGO_EMAIL_BACKEND',
        default='django.core.mail.backends.console.EmailBackend')

SSL_ENABLED = strtobool(os.getenv('SSL_ENABLED', 'False'))
if SSL_ENABLED:
    USE_X_FORWARDED_HOST = True
    if SITEURL.startswith('https'):
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    AVATAR_GRAVATAR_SSL = True