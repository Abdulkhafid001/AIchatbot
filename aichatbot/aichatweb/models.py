# from typing import Self
from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    is_intern = models.BooleanField(default=True)
    # added custom groups to add my specific user groups
    groups = models.ManyToManyField(
        Group,
        related_name='aichatweb_user_set',  # This is the new related name
        blank=True,
    )
    # added custom permission to  my specific user permissions

    user_permissions = models.ManyToManyField(
        Permission, related_name='aichatweb_user_permissions_set', blank=True)


class InternProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name='intern_profile')
    bio = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)


class HRProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name='hr_profile')
    company_name = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
