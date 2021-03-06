#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from django.conf import settings
settings.configure()

import management_audit

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = management_audit.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-management-audit',
    version=version,
    description="""Easily audit Django management commands""",
    long_description=readme + '\n\n' + history,
    author='Dmitry Kozhedubov',
    author_email='dmitry-kozhedubov@yandex.ru',
    url='https://github.com/hiisi13/django-management-audit',
    packages=[
        'management_audit',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-management-audit',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)