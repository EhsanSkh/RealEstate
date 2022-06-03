from django.contrib import admin
from pages.models import Album, Photo
from .models import Realtor
import nested_admin


# class RealtorAlbumPhotoInline(nested_admin.NestedTabularInline):
#     model = Photo
#     extra = 0
#     min_num = 1
#     max_num = 3
#
#
# class RealtorAlbumInline(nested_admin.NestedTabularInline):
#     inlines = (RealtorAlbumPhotoInline,)
#     model = Album
#     exclude = ['listing', 'name']
#     extra = 0
#     min_num = 1
#     max_num = 1
#
#
# class RealtorAdmin(nested_admin.NestedModelAdmin):
#     inlines = (RealtorAlbumInline,)


class RealtorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "hire_date", "is_mvp"]
    list_display_links = ["id", "name", "email"]
    list_editable = ["is_mvp"]
    search_fields = ["name", "email"]
    list_per_page = 20


admin.site.register(Realtor, RealtorAdmin)
