SECRET_KEY = 'dummy'
DEBUG = True
ROOT_URLCONF = 'devops.urls'
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = ['django.contrib.contenttypes', 'django.contrib.staticfiles']
MIDDLEWARE = []
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'db.sqlite3'}}