from django.db import models
from realtors.models import Realtor
from listings.models import Listing
import uuid


class Album(models.Model):
    realtor = models.OneToOneField(Realtor, on_delete=models.CASCADE, null=True, blank=True)
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.realtor:
            return f"(realtor) {self.realtor.name}"
        else:
            return f"(listing) {self.listing.title}"


def upload_photos_dir(instance, file_name):
    ext = file_name.split('.')[-1]
    if instance.album.realtor:
        return "img/uploads/realtors/" + str(uuid.uuid4()) + "." + ext
    else:
        return "img/uploads/listings/" + str(uuid.uuid4()) + "." + ext


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to=upload_photos_dir)

    def __str__(self):
        return str(self.pk)
