#
# Import Django

from django.contrib import admin


#
# Import models

from .models import Userprofile


#
# Register

admin.site.register(Userprofile)