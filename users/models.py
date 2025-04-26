from django.db import models
from django.contrib.auth.models import User

# We're using the built-in Django User model
# Additional user profile functionality can be added here if needed

# Example of extending User model with a profile:
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
