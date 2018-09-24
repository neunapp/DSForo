from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

THUMBNAIL_DEBUG = True
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Unlink', 'TextColor', 'FontSize'],
            ['Smiley', 'Image', 'Iframe'],
            ['RemoveFormat', 'Source'],
        ],
        'height': '100%',
        'width': '100%',
        'youtube_responsive': True,
        'youtube_disabled_fields': [
            'txtWidth',
            'txtHeight',
            'txtEmbed',
        ],
        'extraPlugins': ','.join(['image2',]),
    },
}

# EMAIL SETTINGS
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_secret('EMAIL')
EMAIL_HOST_PASSWORD = get_secret('PASS')
EMAIL_PORT = 587
