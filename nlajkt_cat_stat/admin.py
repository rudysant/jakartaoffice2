from django.contrib import admin

from . models import Catalogues, Acquisition, Book_source, Consignment, Trip_place, Field_trip, Cat_cons, BookRev

class CatalogueA(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_per_page = 10

class Cat_consA(admin.ModelAdmin):
    list_display = ('id', 'consign_no')
    list_per_page = 10

class Book_sourceA(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 10

class AcquisitionA(admin.ModelAdmin):
    list_display = ('id', 'vendor')
    list_per_page = 10

class ConsignmentA(admin.ModelAdmin):
    list_display = ('id', 'consign_no')
    list_per_page = 10

class Trip_placeA(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'category')
    list_per_page = 10

class Field_tripA(admin.ModelAdmin):
    list_display = ('id', 'place', 'status')
    list_per_page = 10

class BookRevA(admin.ModelAdmin):
    list_display = ('id', 'title', 'cover')
    list_per_page = 10


admin.site.register(Catalogues, CatalogueA)
admin.site.register(Book_source, Book_sourceA)
admin.site.register(Acquisition, AcquisitionA)
admin.site.register(Consignment, ConsignmentA)
admin.site.register(Trip_place, Trip_placeA)
admin.site.register(Field_trip, Field_tripA)
admin.site.register(Cat_cons, Cat_consA)
admin.site.register(BookRev, BookRevA)


# Register your models here.
