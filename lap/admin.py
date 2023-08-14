from django.contrib import admin

# Register your models here.
from .models import Laptop, kpi, repair

# Register your models here.
admin.site.register(Laptop)

admin.site.register(kpi)

admin.site.register(repair)