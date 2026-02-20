from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser,PermissionsMixin)
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class UserManager(BaseUserManager):
    # Custom manager for User model
    def create_user(self,email,password,**extra_fields):
        # Create and save a regular user with the given email and password and extra_fields.
        if not email:
            raise ValueError(_("The email must be set."))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields):
        # Create and save a superuser with the given email and password.
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)

        if extra_fields.get("is_staff") is not True:
         raise ValueError(_("Superuser must have is_staff=True."))

        if extra_fields.get("is_superuser") is not True:
         raise ValueError(_("Superuser must have is_superuser=True."))
        
        return self.create_user(email,password,**extra_fields)
class User(AbstractBaseUser,PermissionsMixin):
    # Custom User model.
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_verifield = models.BooleanField(default=True)
    first_name = models.CharField(max_length=20)

    # login identifier
    USERNAME_FIELD = "email"

    # extra fields for superuser
    REQUIRED_FIELDS = []

    objects = UserManager()

    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        # Display user email as string representation.
        return self.email
    
class Profile(models.Model):
   # Profile for creating user info from User model
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   first_name = models.CharField(max_length=255)
   last_name = models.CharField(max_length=255)
   image = models.ImageField(blank=True, null=True)
   description = models.TextField()
   created_date = models.DateField(auto_now_add=True)
   updated_date = models.DateField(auto_now=True)

   def __str__(self):
      # String representation of the profile
      return self.user.email

@receiver(post_save, sender=User)
# Automatically create a Profile when a new User is created
def save_profile(sender, instance, created, **kwargs):
   # Only create a Profile for newly created Users
   if created:
      Profile.objects.create(user=instance)