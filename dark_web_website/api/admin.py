from django.contrib import admin
from .models import vehicleStatus


class vehicleStatusAdmin(admin.ModelAdmin):
    list_display = ('vehicleid',)


admin.site.register(vehicleStatus, vehicleStatusAdmin)
