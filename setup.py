#!/usr/bin/env python

from setuptools import setup

setup(
    name='BCDF',
    version='2.0',
    description='BCDF Web App',
    author='Adonis Bovell',
    author_email='yoshimitsu12@gmail.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=[
        'Django==1.8.18',
        'Pillow==2.7.0',
        'python-memcached==1.53',
        'django-recaptcha==1.0.4',
        'psycopg2==2.7.3.1'
    ],
)
