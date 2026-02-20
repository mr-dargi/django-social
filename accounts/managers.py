from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """ 
    Custom user manager for CustomUser model.
    Handels user and superuser creation using email as the login identifier.
    """

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Email is required"))
        
        user = self.model(
            email= self.normalize_email(email),
            username = username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        # Force required admin flags
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)

        # test for is_superuser became true then will access for create superuser
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("There is problem to making super user!"))
        
        return self.create_user(email, username, password, **extra_fields)
        
