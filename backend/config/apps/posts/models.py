from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Post(models.Model):
    class Meta(object):
        db_table= 'post'


    name = models.CharField(
        'Name', blank=False, null=False, max_length=15, db_index=True, default='Anonymous'
    )

    body= models.CharField(
        'Body', blank=False, null=False, max_length=500, db_index=True
    )

    image=CloudinaryField(
        'image', blank=True, null=True

    )

    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )