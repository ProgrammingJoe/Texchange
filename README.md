# Texchange

A web application designed to make textbook exchange at universities easier.

The application can be found at: http://www.texchange.ca/

# Additional Settings Required to Run Locally
#### Tips
* Put these settings in a file called secret_settings.py in the exchange folder
* You will need to create a [Facebook app](https://developers.facebook.com/) and API key to get login working
* You can also setup a [Google app](https://console.developers.google.com) with an API key to get Google login working.
* You can use [ngrok](https://ngrok.com/) to get the login working as it will not work using 127.0.0.1/port as the target address in the Facebook app settings or the Google app settings.
* Don't forget to update `Pathtoprojectfolder` in MEDIA_ROOT and STATIC_URL

#### Settings.py

```python
import os
from secret_settings import *

SECRET_KEY = ''
DEBUG = True
ALLOWED_HOSTS = [".ngrok.io"]
SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_ROOT = 'pathtoprojectfolder/Texchange/textchange/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = 'pathtoprojectfolder/Texchange/textchange/static/'
STATIC_URL = '/static/'
```
