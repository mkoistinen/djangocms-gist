#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from djangocms_gist import __version__


INSTALL_REQUIRES = [
    'django-easy-select2>=1.3.2',
    'django-cms>=3.1',
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 1.8',
    'Framework :: Django :: 1.9',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

setup(
    name='djangocms-gist',
    version=__version__,
    description='Gist Plugin for django CMS',
    author='Martin Koistinen',
    author_email='mkoistinen@gmail.com',
    url='https://github.com/mkoistinen/djangocms-gist',
    packages=['djangocms_gist', 'djangocms_gist.migrations'],
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False
)
