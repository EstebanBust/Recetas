from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    description = models.TextField()
    instructions = models.TextField()
    created_by = models.CharField(max_length=50)
    image1 = models.URLField(null=True, blank=True)
    image2 = models.URLField(null=True, blank=True)
    image3 = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name