from django.contrib import admin

<<<<<<< HEAD
# Register your models here.

from .models import *

admin.site.register(Land)
admin.site.register(Farmer)
admin.site.register(Investor)
=======
from finance.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Land)
>>>>>>> 20eb7e3bb2e7cbacc099e1e04e2f96eb6b410657
