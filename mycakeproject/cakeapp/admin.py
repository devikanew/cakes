from django.contrib import admin

# Register your models here.
from cakeapp.models import City, Town


class CityAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(City, CityAdmin)


class TownAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Town, TownAdmin)
