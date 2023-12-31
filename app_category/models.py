from django.db import models
from base.models import BaseModel

# Create your models here.
class Category(BaseModel):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank= True)
    category_description = models.TextField()
    is_available = models.BooleanField()