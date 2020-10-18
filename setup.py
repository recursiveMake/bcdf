#!/usr/bin/env python

from setuptools import setup

setup(
    name='BCDF',
    version='3.0',
    description='BCDF Web App',
    author='Adonis Bovell',
    author_email='yoshimitsu12@gmail.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=[
        'boto3==1.12.49',
        'Django==3.0.7',
        'Pillow==8.0.0',
        'python-memcached==1.59',
        'django-recaptcha==2.0.6',
        'django-storages==1.9.1',
        'psycopg2==2.8.6'
    ],
)
