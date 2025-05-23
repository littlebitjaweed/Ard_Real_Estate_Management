from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    property_type = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='property_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

