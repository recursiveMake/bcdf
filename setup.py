#!/usr/bin/env python

from setuptools import setup

setup(
    name='BCDF',
    version='2.1',
    description='BCDF Web App',
    author='Adonis Bovell',
    author_email='yoshimitsu12@gmail.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=[
        'Django==1.11.20',
        'Pillow==6.0.0',
        'python-memcached==1.59',
        'django-recaptcha==2.0.4',
        'django-storages==1.7.1',
        'psycopg2==2.8.2'
    ],
)
