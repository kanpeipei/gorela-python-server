from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.
class AccountsManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Create and save a user with the given username, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Accounts(AbstractBaseUser):

    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    # password = models.CharField(max_length=50, blank=True, null=True)
    introduction = models.TextField(max_length=254, blank=True, null=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountsManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

        
    # is_superuser:なんやこれ
    # @property
    # def is_superuser(self):
    #     return self.is_admin

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = "accounts"
        verbose_name_plural = "Accounts"

