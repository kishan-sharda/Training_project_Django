from django.contrib import admin
from django.db import models
from .models import banners, user, watches
# Register your models here.


admin.site.register(watches)
admin.site.register(banners)

class TimupsAdminArea(admin.AdminSite):
    site_header = 'Timups Admin Area'

timups_site =  TimupsAdminArea(name='TimupsAdmin')

timups_site.register(watches)
timups_site.register(user)