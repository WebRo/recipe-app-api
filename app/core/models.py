from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    """Class required by Django for managing our users from the management
    command.
    """
    

    def create_user(self, email, name, password=None, **other_fields):
        """Creates a new user with the given detials."""

        #email=self.normalize_email(email)
        

        # Check that the user provided an email.
        if not email:
            raise ValueError('Users must have an email address.')

        # Create a new user object.
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            password=password,
            **other_fields,
        )

        # Set the users password. We use this to create a password
        # hash instead of storing it in clear text.
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, name, email, password):
        """create and save sa new super user"""  
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)

        return user



    


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support useing email instead of username""" 

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    USERNAME_FIELD = 'email'









































# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# # Create your models here.


# class UserManager(BaseUserManager):

#     def create_user(self, email, password=None, **other_fields):
#         """Create and save a new user"""
        
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             #email=self.normalize_email(email),
#             email=email,
#             **other_fields,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser, PermissionsMixin):
#     """Custom user model that support useing email instead of username""" 

#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)


#     REQUIRED_FIELDS = ['name']

#     objects = UserManager()

#     USERNAME_FIELD = 'email'

