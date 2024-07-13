from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Movie (models.Model):
    title= models.CharField(max_length=30, null=False)
    genre = models.CharField(max_length=30, null=False)
    director_name = models.CharField(max_length=30, null=False)
    publication_year = models.IntegerField(null=False)
    sipnosis = models.TextField (null=False)
    
    def __str__(self) -> str:
        return self.title