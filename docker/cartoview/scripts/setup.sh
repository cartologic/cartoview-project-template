#!/usr/bin/env bash


# Update the package listing, so we know what package exist:
apt-get update -y

# Install security updates:
apt-get -y upgrade

apt-get install wget gnupg -y

# add postgres client 11.2
echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" | tee /etc/apt/sources.list.d/pgdg.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

# add gdal repo
echo "deb http://http.us.debian.org/debian buster main non-free contrib" >>/etc/apt/sources.list

# geonode required libraries
apt-get update && apt-get install -y \
		gcc zip \
		gettext \
		postgresql-client-11 libpq-dev \
		sqlite3 spatialite-bin libsqlite3-mod-spatialite \
                python3-gdal python3-psycopg2 python3-ldap \
                python3-pil python3-lxml python3-pylibmc \
                python3-dev libgdal-dev \
                libxml2 libxml2-dev libxslt1-dev zlib1g-dev libjpeg-dev \
                libmemcached-dev libsasl2-dev \
                libldap2-dev libsasl2-dev \
                uwsgi uwsgi-plugin-python3 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

# update python pip version
pip install --upgrade pip

# Update C env vars so compiler can find gdal
CPLUS_INCLUDE_PATH=/usr/include/gdal
C_INCLUDE_PATH=/usr/include/gdal

#let's install pygdal wheels compatible with the provided libgdal-dev
gdal-config --version | cut -c 1-5 | xargs -I % pip install 'pygdal>=%.0,<=%.999'

# install geoip-bin
printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
apt-get update && apt-get install -y geoip-bin


# install cartoview
cd /tmp
git clone https://github.com/cartologic/cartoview.git
cd cartoview
pip install .
cd /tmp
rm -rf cartoview

# Installing extra python packages required for CartoView Apps:
cd /cartoview_scripts
pip install -r extra_req.txt

# cleanup image
rm -rf ~/.cache/pip
rm -rf /root/.cache
apt-get purge --auto-remove -y gcc libgdal-dev libsasl2-dev \
	zlib1g-dev python-dev build-essential
apt autoremove --purge -y && apt autoclean -y && apt-get clean -y
rm -rf /var/lib/apt/lists/* && apt-get clean -y &&
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
echo "Yes, do as I say!" | apt-get remove --force-yes login &&
	dpkg --remove --force-depends wget
