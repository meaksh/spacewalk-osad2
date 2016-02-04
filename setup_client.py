#!/usr/bin/env python

from distutils.core import setup
import os

OSAD2_PATH = os.path.dirname(os.path.realpath(__file__))
PKGNAME = 'spacewalk-osad2-client'
PKGNAME_FILE = os.path.join(OSAD2_PATH, "PKGNAME")

DATA_FILES = [
   ('/etc/rhn/osad2-client/', ['etc/osad_client.prod.cfg']),
]


if os.path.isfile(PKGNAME_FILE):
    client_name = open(PKGNAME_FILE, "r").readline().strip()
    PKGNAME += "-" + client_name

    client_key = 'etc/%s.key_secret' % client_name
    server_key = 'etc/server.key'

    DATA_FILES.extend([
        ('/etc/rhn/osad2-client/certs/', [client_key, server_key]),
    ])


setup(name=PKGNAME,
      version='alpha',
      license='GPLv2',
      description='An alternative OSA dispatcher module for Spacewalk',
      long_description='This is an experiment to improve osad, a service that '
                       'simulates instant execution of actions in a Spacewalk '
                       'environment.',

      platforms=['All'],

      packages=['osad2', 'osad2.client'],
      scripts=['bin/osad2_client.py'],

      data_files=DATA_FILES)
