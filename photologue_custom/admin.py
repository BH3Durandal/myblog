from django.contrib import admin

# Register your models here.
from photologue.admin import GalleryAdmin
from photologue.models import Gallery


class GalleryAdmin(GalleryAdmin):

    filter_horizontal = ('photos',)

admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)