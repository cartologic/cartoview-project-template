# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2018 OSGeo
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
import json
import os
import re
import sys

from paver.easy import path, task

try:
    from paver.path import pushd
except ImportError:
    from paver.easy import pushd

assert sys.version_info >= (2, 6), \
    SystemError("Cartoview Build requires python 2.6 or better")


@task
def install_docker_data_dir():
    siteurl = os.environ.get('SITEURL', 'http://localhost/')
    geoserver_location = os.environ.get('GEOSERVER_LOCATION', "http://geoserver:8080/")
    nginx_location = os.environ.get("NGINX_LOCATION", "http://nginx:80/")

    geoserver_data_dir = path('/geoserver_data/data')
    global_conf = os.path.join(geoserver_data_dir, 'global.xml')
    security_filter_conf = os.path.join(geoserver_data_dir, path('security/filter/geonode-oauth2/config.xml'))
    security_role_conf = os.path.join(geoserver_data_dir, path('security/role/geonode REST role service/config.xml'))

    try:
        config = global_conf
        with open(config) as f:
            xml = f.read()
            m = re.search('proxyBaseUrl>([^<]+)', xml)
            xml = xml[:m.start(1)] + \
                  "{}geoserver".format(geoserver_location) + xml[m.end(1):]
            with open(config, 'w') as f:
                f.write(xml)
    except Exception as e:
        print('Error while modifying {} :'.format(security_role_conf), e)

    try:
        config = security_filter_conf
        with open(config) as f:
            xml = f.read()
            m = re.search('accessTokenUri>([^<]+)', xml)
            xml = xml[:m.start(1)] + \
                  "{}o/token/".format(nginx_location) + xml[m.end(1):]
            m = re.search('userAuthorizationUri>([^<]+)', xml)
            xml = xml[:m.start(
                1)] + "{}o/authorize/".format(siteurl) + xml[m.end(1):]
            m = re.search('redirectUri>([^<]+)', xml)
            xml = xml[:m.start(
                1)] + "{}geoserver/index.html".format(siteurl) + xml[m.end(1):]
            m = re.search('checkTokenEndpointUrl>([^<]+)', xml)
            xml = xml[:m.start(
                1)] + "{}api/o/v4/tokeninfo/".format(nginx_location) + xml[m.end(1):]
            m = re.search('logoutUri>([^<]+)', xml)
            xml = xml[:m.start(
                1)] + "{}account/logout/".format(siteurl) + xml[m.end(1):]
            with open(config, 'w') as f:
                f.write(xml)
    except Exception as e:
        print('Error while modifying {} :'.format(security_filter_conf), e)

    try:
        config = security_role_conf
        with open(config) as f:
            xml = f.read()
            m = re.search('baseUrl>([^<]+)', xml)
            xml = xml[:m.start(1)] + nginx_location[:-1] + xml[m.end(1):]
            with open(config, 'w') as f:
                f.write(xml)
    except Exception as e:
        print('Error while modifying {} :'.format(security_role_conf), e)


@task
def prepare_docker_oauth_fixture():
    project_name = os.environ.get('PROJECT_NAME', 'cartoview')
    fixturefile = path('{}/fixtures/default_oauth_apps_docker.json'.format(project_name))
    os.remove(fixturefile)
    siteurl = os.environ.get('SITEURL', 'http://localhost/')
    default_fixture = [
        {
            "model": "oauth2_provider.application",
            "pk": 1001,
            "fields": {
                "skip_authorization": True,
                "created": "2018-05-31T10:00:31.661Z",
                "updated": "2018-05-31T11:30:31.245Z",
                "algorithm": "RS256",
                "redirect_uris": "{}geoserver/index.html".format(siteurl),
                "name": "GeoServer",
                "authorization_grant_type": "authorization-code",
                "client_type": "confidential",
                "client_id": "Jrchz2oPY3akmzndmgUTYrs9gczlgoV20YPSvqaV",
                "client_secret": "\
rCnp5txobUo83EpQEblM8fVj3QT5zb5qRfxNsuPzCqZaiRyIoxM4jdgMiZKFfePBHYXCLd7B8NlkfDB\
Y9HKeIQPcy5Cp08KQNpRHQbjpLItDHv12GvkSeXp6OxaUETv3",
                "user": [
                    "admin"
                ]
            }
        }
    ]
    with open(fixturefile, 'w') as ff:
        json.dump(default_fixture, ff)
