try:
    from pre_settings import *
except:
    pass
import os
import cartoview
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)
cartoview_settings_path = os.path.join(os.path.dirname(cartoview.__file__), 'settings.py')
execfile(cartoview_settings_path)

MEDIA_ROOT = os.path.join(BASE_DIR, "uploaded")
MEDIA_URL = "/uploaded/"
LOCAL_MEDIA_URL = "/uploaded/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS += [os.path.join(PROJECT_DIR, "static"),]

try:
    from local_settings import *
except:
    pass
