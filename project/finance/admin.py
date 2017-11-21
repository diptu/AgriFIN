from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Land)
admin.site.register(Farmer)
admin.site.register(Investor)
