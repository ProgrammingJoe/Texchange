# Texchange

A web application designed to make textbook exchange at the University of Victoria easy.

The application can be found at: http://www.texchange.ca/

# Additional Settings Required to Run Locally
####Tips
* Put these settings in a file called settings.py in the exchange folder
* You will need to create a Facebook app to get login working (https://developers.facebook.com/)
* You can use ngrok from https://ngrok.com/ to get the Facebook login working as it will not work using 127.0.0.1/port as the target address in the Facebook app settings
* Don't forget to update pathtoprojectfolder in MEDIA_ROOT and STATIC_URL

####Settings.py

* import os
* from base_settings import *
* BASE_DIR = os.path.dirname(os.path.abspath(__file__))
* SECRET_KEY = ''
* DEBUG = True
* ALLOWED_HOSTS = [".ngrok.io"]
* SOCIAL_AUTH_FACEBOOK_KEY = ''
* SOCIAL_AUTH_FACEBOOK_SECRET = ''
* DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
* MEDIA_ROOT = 'pathtoprojectfolder/Texchange/textchange/media/'
* MEDIA_URL = '/media/'
* STATIC_ROOT = 'pathtoprojectfolder/Texchange/textchange/static/'
* STATIC_URL = '/static/'
