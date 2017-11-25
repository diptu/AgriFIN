from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from finance.models import *
# Register your models here.

# admin.site.register(User, UserAdmin)
admin.site.register(User)

admin.site.register(Land)

admin.site.register(Branch)

admin.site.register(Share)

admin.site.register(Crop)

admin.site.register(Fertilizer)
