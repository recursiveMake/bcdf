#!/usr/bin/env python

from setuptools import setup

setup(
    name='BCDF',
    version='1.0',
    description='BCDF Web App',
    author='Adonis Bovell',
    author_email='yoshimitsu12@gmail.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django==1.7.3', 'Pillow==2.7.0', 'django_compressor==1.4', 'python-memcached==1.53'],
)
