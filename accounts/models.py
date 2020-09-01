from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class CustomUser(AbstractUser):
    
    
    class Meta:
        pass
    def main__str__(self):
        return self.username
    