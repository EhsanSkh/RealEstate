from django.shortcuts import render
from django.views import generic
from .models import Listing


class ListingsView(generic.ListView):
    template_name = "listings/listings.html"
    model = Listing
    context_object_name = "listings"
    paginate_by = 6

    def get_queryset(self):
        return Listing.objects.published().order_by("-list_date")


class ListingView(generic.DetailView):
    template_name = "listings/listing.html"
    model = Listing

    def get_context_data(self, **kwargs):
        context = super(ListingView, self).get_context_data(**kwargs)
        photos = []
        for photo in self.object.album.photos.all():
            photos.append(photo.image.url)
        context["main_photo"] = photos[0]
        context["photos"] = photos[1:]
        if self.object.realtor.is_mvp:
            mvp = self.object.realtor
        else:
            mvp = False
        context["mvp"] = mvp
        return context
