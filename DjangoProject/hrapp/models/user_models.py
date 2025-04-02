from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.base_user import BaseUserManager
from .custom_manager import *
# Custom User Model

# Custom Managers
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class UserManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)  # Example: Only active users

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    supervisor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    is_deleted = models.BooleanField(default=False)  # ✅ Soft delete field

    def delete(self, *args, **kwargs):
        """Soft delete the user instead of permanently deleting it."""
        self.is_deleted = True
        self.save()

    def restore(self):
        """Restore a soft-deleted user."""
        self.is_deleted = False
        self.save()
    objects = UserManager()  # Custom manager   # Only active users

    all_objects = models.Manager()  # this to get all users (including deleted)
    active_objects = ActiveManager()
    soft_deleted_objects = SoftDeleteManager()

    def __str__(self):
        return self.email

    @property
    def role(self):
        """Return the first group name as the role."""
        return self.groups.first().name if self.groups.exists() else None

    class Meta:
        permissions = [
            #Add Custom Permissions Here

        ]






