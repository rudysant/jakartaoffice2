from django.contrib import admin

from . models import Catalogues

class CataloguesA(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_per_page = 10

    

admin.site.register(Catalogues, CataloguesA)



# Register your models here.
