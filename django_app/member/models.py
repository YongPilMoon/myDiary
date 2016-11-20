from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class DiaryUserManager(BaseUserManager):
    def create_user(
            self,
            email,
            nickname,
            password=None,
            ):
        user = self.model(
            email=email,
            nickname=nickname,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
            self,
            email,
            nickname,
            password=None,
            ):
        user = self.model(
            email=email,
            nickname=nickname,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class DiaryUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    nickname = models.CharField(max_length=24)
    is_staff = models.BooleanField(default=False)

    objects = DiaryUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.nickname

    def get_short_name(self):
        return self.nickname

