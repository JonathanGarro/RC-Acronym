from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Acronym(models.Model):
    acronym = models.CharField(max_length=50)
    definition = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.acronym} - {self.definition}"
    
    def get_absolute_url(self):
        return reverse('acronym-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['acronym']
        verbose_name_plural = "Acronyms"
