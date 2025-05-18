from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# National Society model
class NationalSociety(models.Model):
    national_society_id = models.CharField(max_length=50, unique=True)
    go_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "National Societies"


# Extending User model with a profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # Add your new fields here
    department = models.CharField(max_length=100, blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    national_society = models.ForeignKey(NationalSociety, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


# Create Profile automatically when User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
