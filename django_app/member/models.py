from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class DiaryUserManager(UserManager):
    pass


class DiaryUser(AbstractUser):

    objects = DiaryUserManager()

    def __str__(self):
        return self.username
