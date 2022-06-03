from django.contrib import admin
from .models import Album, Photo
import nested_admin


class AlbumPhotoInline(nested_admin.NestedTabularInline):
    model = Photo
    extra = 0
    min_num = 1
    max_num = 6


class AlbumAdmin(nested_admin.NestedModelAdmin):
    inlines = (AlbumPhotoInline,)


admin.site.register(Album)
admin.site.register(Photo)
