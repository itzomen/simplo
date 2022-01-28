from django.db import models
from versatileimagefield.fields import VersatileImageField



class Category(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True)
    image = VersatileImageField(upload_to="categories", blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)