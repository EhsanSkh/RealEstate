from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from listings.models import Listing
from realtors.models import Realtor


class HomeView(generic.ListView):
    template_name = "pages/home.html"
    model = Listing
    context_object_name = "listings"

    def get_queryset(self):
        return Listing.objects.published().order_by("-list_date")[:3]


class AboutView(generic.ListView):
    template_name = "pages/about.html"
    model = Realtor
    context_object_name = "realtors"

    def get_queryset(self):
        queryset = super(AboutView, self).get_queryset()
        return queryset.order_by("-hire_date")

    def get_context_data(self, *args, **kwargs):
        context = super(AboutView, self).get_context_data(*args, **kwargs)
        mvp = Realtor.objects.filter(is_mvp=True).first()
        context["mvp"] = mvp
        return context


class SearchView(generic.ListView):
    template_name = "pages/home.html"
    model = Listing
    context_object_name = "listings"

    def get_queryset(self):


        listings = Listing.objects.published().filter(
            Q(description__icontains=self.request.GET.get("keywords")) |
            Q(realtor__name__icontains=self.request.GET.get("keywords")) |
            Q(city__icontains=self.request.GET.get("city")) |
            Q(state__icontains=self.request.GET.get("state")) |
            Q(bedrooms__iexact=self.request.GET.get("bedrooms")) |
            Q(price__lte=self.request.GET.get("price"))
        )

        return listings.order_by("-list_date")
