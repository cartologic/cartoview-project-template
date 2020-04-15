#!/usr/bin/env bash

apt-get update -y && apt-get install wget gnupg -y

# add postgres client latest
touch /etc/apt/sources.list.d/pgdg.list &&
	echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" >>/etc/apt/sources.list.d/pgdg.list &&
	wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

# add gdal repo
echo "deb http://http.us.debian.org/debian buster main non-free contrib" >>/etc/apt/sources.list

# geonode required libraries
apt-get update -y && apt-get install -y \
	build-essential gcc git \
	libxml2-dev libxslt1-dev libxslt-dev python-dev \
	gettext sqlite3 \
	python-lxml \
	postgresql-client libpq-dev python-psycopg2 \
	python-pil \
	python-ldap \
	libmemcached-dev libsasl2-dev \
	python-pylibmc \
	gdal-bin libgdal-dev libgeos-dev \
	--no-install-recommends

# update python pip version
pip install --upgrade pip

# install python gdal stable
pip install GDAL==2.3.2

# install cartoview
cd /tmp
git clone https://github.com/cartologic/cartoview.git
cd cartoview
pip install .
cd /tmp
rm -rf cartoview

# Installing extra python packages required for CartoView Apps:
cd /cartoview_scripts
pip install extra_req.txt

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
