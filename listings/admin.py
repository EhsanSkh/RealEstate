from django.contrib import admin
from pages.models import Album, Photo
from .models import Listing
import nested_admin


# class ListingAlbumPhotoInline(nested_admin.NestedTabularInline):
#     model = Photo
#     extra = 0
#     min_num = 1
#     max_num = 6
#
#
# class ListingAlbumInline(nested_admin.NestedTabularInline):
#     inlines = (ListingAlbumPhotoInline,)
#     model = Album
#     exclude = ['realtor', 'name']
#     extra = 0
#     min_num = 1
#     max_num = 1
#
#
# class ListingAdmin(nested_admin.NestedModelAdmin):
#     inlines = (ListingAlbumInline,)


class ListingAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "realtor", "price", "list_date", "is_published"]
    list_display_links = ["id", "title"]
    list_editable = ["is_published"]
    list_filter = ["realtor", "is_published"]
    search_fields = ["title", "description", "address", "city", "state"]
    list_per_page = 20


admin.site.register(Listing, ListingAdmin)
