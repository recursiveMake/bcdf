# -*- coding: utf-8 -*-
# Django settings for OpenShift project.
import os

# a setting to determine whether we are running on OpenShift
ON_AWS = False
if os.environ.has_key('AWS'):
    ON_AWS = True

DEPLOY = False
if os.environ.has_key('DEPLOY'):
    DEPLOY = True

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = os.path.join(PROJECT_DIR, os.pardir)

if ON_AWS:
    DEBUG = False
else:
    DEBUG = True

if DEBUG:
    print("WARNING: The DEBUG environment is set to True.")

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('adonis', 'yoshimitsu12@gmail.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('RDS_DB_NAME', 'bcdf-db'),
        'HOST': os.environ.get('RDS_HOSTNAME', 'localhost'),
        'PORT': os.environ.get('RDS_PORT', '5432'),
        'USER': os.environ.get('RDS_USERNAME', 'bcdf'),
        'PASSWORD': os.environ.get('RDS_PASSWORD')
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
if ON_AWS:
    MEDIA_ROOT = ''
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'local', 'media')

if ON_AWS:
    AWS_STATIC_STORAGE_BUCKET_NAME = 'bcdf-bucket'
    AWS_MEDIA_STORAGE_BUCKET_NAME = 'bcdf-media-bucket'
    AWS_QUERYSTRING_AUTH = False
    S3_URL_TEMPLATE = 'https://%s.s3.amazonaws.com/'

    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
    AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'us-east-1')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
if ON_AWS:
    DEFAULT_FILE_STORAGE = 'bcdf.custom_storages.MediaStorage'
    MEDIA_URL = S3_URL_TEMPLATE % AWS_MEDIA_STORAGE_BUCKET_NAME
else:
    MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
if ON_AWS:
    STATICFILES_STORAGE = 'bcdf.custom_storages.StaticStorage'
    STATIC_URL = S3_URL_TEMPLATE % AWS_STATIC_STORAGE_BUCKET_NAME
else:
    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'vm4rl5*ymb@2&d_(gc$gb-^twq9w(u69hi--%$5xrh!xk(t%hw')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'website.middleware.ProductionServer',
)

ROOT_URLCONF = 'bcdf.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'django.contrib.sitemaps',
    'captcha',
    'storages'
)

if DEPLOY:
    INSTALLED_APPS += (
        'django.contrib.admin',
        'django.contrib.admindocs'
    )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
if ON_AWS:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

if not ON_AWS:
    TEMPLATE_CONTEXT_PROCESSORS += ("django.core.context_processors.debug", )

if ON_AWS:
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_USER', 'root@localhost')
    SERVER_EMAIL = os.environ.get('EMAIL_USER', 'root@localhost')
    EMAIL_USE_TLS = False
    EMAIL_HOST = 'smtpout.secureserver.net'
    EMAIL_PORT = 80
    EMAIL_HOST_USER = os.environ.get('EMAIL_USER', 'root')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS', '')

if ON_AWS:
    # TODO: Configure memcached
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
            # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            # 'LOCATION': 'unix:' + os.path.join(
            #     os.environ.get('OPENSHIFT_TMP_DIR'),
            #     'cache_file.sock'
            # ),
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
        }
    }

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

NOCAPTCHA = True
RECAPTCHA_USE_SSL = True
RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')


if not DEBUG and not DEPLOY:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
