from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model using email as the uniqe identifier.
    Includes basic authentication flags and custom manager.
    """
    email = models.EmailField(max_length=255, unique=True, verbose_name=_("email address"))
    username = models.CharField(max_length=100, unique=True)
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    # Authentication and admin permissions
    is_active = models.BooleanField(default=True, verbose_name=_("active"))
    is_staff = models.BooleanField(default=False, verbose_name=_("staff status"))
    is_admin = models.BooleanField(default=False, verbose_name=_("admin status"))

    date_join = models.DateTimeField(auto_now_add=True, verbose_name=_("date joined"))

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email