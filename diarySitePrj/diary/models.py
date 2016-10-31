from django.db import models
from diarySite.settings import AUTH_USER_MODEL


class Diary(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    author = models.ForeignKey(AUTH_USER_MODEL)
    written_date = models.DateField()

    def __str__(self):
        return self.title

