from django.urls import path
from . import views

app_name = "listing"

urlpatterns = [
    path('', views.ListingsView.as_view(), name="list"),
    path('<int:pk>/', views.ListingView.as_view(), name="detail"),
]
