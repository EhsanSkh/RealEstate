from django.db.models.signals import post_save
from realtors.models import Realtor
from listings.models import Listing
from .models import Album


def post_save_create_realtor_album(sender, instance, created, *args, **kwargs):
    Album.objects.get_or_create(realtor=instance)


post_save.connect(post_save_create_realtor_album, sender=Realtor)


def post_save_create_realtor_album(sender, instance, created, *args, **kwargs):
    Album.objects.get_or_create(listing=instance)


post_save.connect(post_save_create_realtor_album, sender=Listing)
