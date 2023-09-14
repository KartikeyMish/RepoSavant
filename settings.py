ALLOWED_HOSTS = ['.vercel.app', 'row.sh']

import os

STATICFILES_DIRS = os.path.join('.', 'static')
STATIC_ROOT = os.path.join('.', 'staticfiles_build', 'static')