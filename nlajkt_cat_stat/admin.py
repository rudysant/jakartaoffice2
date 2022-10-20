from django.contrib import admin

from . models import Catalogues, Acquisition2, Book_source, Consignment

class CataloguesA(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_per_page = 10

class Book_sources(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 10

class AcquisitionA(admin.ModelAdmin):
    list_display = ('id', 'vendor')
    list_per_page = 10

class ConsignmentA(admin.ModelAdmin):
    list_display = ('id', 'consign_no')
    list_per_page = 10

admin.site.register(Catalogues, CataloguesA)
admin.site.register(Book_source, Book_sources)
admin.site.register(Acquisition2, AcquisitionA)
admin.site.register(Consignment, ConsignmentA)

# Register your models here.
