from django.contrib import admin

from . models import Catalogues, Acquisition

class CataloguesA(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_per_page = 10

class AcquisitionA(admin.ModelAdmin):
    list_display = ('id', 'vendor')
    list_per_page = 10



admin.site.register(Catalogues, CataloguesA)
admin.site.register(Acquisition, AcquisitionA)


# Register your models here.
