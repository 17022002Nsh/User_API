from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    address = models.CharField(max_length=200, blank=True, null=True)
    
    
    def __str__(self):
        return self.username
    
    
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, default=uuid.uuid4(), unique=True)
    
    
class Book(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    page_num = models.PositiveIntegerField(default=1)
    
        
    
    
    
    
