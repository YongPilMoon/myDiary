from django.db import models
from diarySite.settings import AUTH_USER_MODEL
from versatileimagefield.fields import VersatileImageField


class Diary(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    author = models.ForeignKey(AUTH_USER_MODEL)
    diary_date = models.DateField()

    def __str__(self):
        return self.title


class ExampleModel(models.Model):
    image = VersatileImageField(
        'Image',
        upload_to='photo/'
    )