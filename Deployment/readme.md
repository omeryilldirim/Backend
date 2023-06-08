<!--
    0  cd ~
    1  rm -rf *
    2  git clone https://github.com/omeryilldirim/FlightAPI.git
    3  cd FlightAPI/
    4  python -m venv env
    5  source env/bin/activate
    6  pip install -r requirements.txt
    7  mkdir static
    8  python manage.py collectstatic
    9  python manage.py migrate
   10  python manage.py createsuperuser




# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/QadirAdamson/mysite/mysite/settings.py'
# and your manage.py is is at '/home/QadirAdamson/mysite/manage.py'
path = '/home/QadirAdamson/FlightAPI'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
-->