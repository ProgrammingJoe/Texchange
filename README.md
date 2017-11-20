# Texchange

A web application designed to make textbook exchange at universities easier.

The application can be found at: http://www.texchange.ca/

## What is Texchange?

Texchange is a web platform that I began working on a couple years ago because I was tired of watching people pay ridiculous amounts of money for textbooks. I knew of multiple UVic Facebook groups that allowed UVic students to post textbooks for sale but postings often got lost as everything was sorted chronologically. This was my first big side project so please excuse any bad code practices that I haven't managed to find the time to fix :).

## How can I contribute?

I'm not actively working on this project anymore but everyone is free to make contributions :). If you want to clean up the code, add new features, or add new school scraping scripts please make a pull request so myself or others can review your changes.

## How to get started?

* Create and activate a virtual environment
  * `$ pip install virtualenv`
  * `$ python -m virtualenv venv` or whatever name you want instead of venv.
  * `$ source venv/bin/activate`
* Install python dependencies
  * `$ pip install -r requirements.txt`

* Put these settings in a file called secret_settings.py in the exchange folder

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

#### Tips
* You will need to create a [Facebook app](https://developers.facebook.com/) and API key to get login working
* You can also setup a [Google app](https://console.developers.google.com) with an API key to get Google login working.
* You can use [ngrok](https://ngrok.com/) to get the login working as it will not work using 127.0.0.1/port as the target address in the Facebook app settings or the Google app settings.
* Don't forget to update `Pathtoprojectfolder` in MEDIA_ROOT and STATIC_URL

## Where do I go for help?

I have no official documentation for this app but if you need help with anything feel free to tweet at me or send me a message on [Twitter](https://twitter.com/BanJoe_Kazooie).
