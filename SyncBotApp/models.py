from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    cnic = models.CharField(max_length=15, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True, help_text="Enter your full address")
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=10, null=True, blank=True)
    verification_code_expiry = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'age': self.age,
            'cnic': self.cnic,
            'phone_number': self.phone_number,
            'address': self.address,
            'profile_picture': self.profile_picture.url if self.profile_picture else None,
            'is_verified': self.is_verified
        }