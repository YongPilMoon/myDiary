from django.db import models
from diarySite.settings import AUTH_USER_MODEL


class Diary(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    author = models.ForeignKey(AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return self.title

