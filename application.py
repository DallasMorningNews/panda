#!/usr/bin/env python

import os, sys

import django.core.handlers.wsgi

sys.path.append('/opt/panda')


# When serving under WSGI (rather than runserver) use deployed config
os.environ["DJANGO_SETTINGS_MODULE"] = "config.deployed.settings"

application = django.core.handlers.wsgi.WSGIHandler()

