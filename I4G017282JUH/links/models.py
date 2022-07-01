from django.db import models
from django.contrib.auth import get_user_model 

# Create your models here.

class Link(models.Model):

    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, editable=False, unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="author")
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(editable=True)

    def __str__(self):
        return self.target_url