from django.db import models
from django.utils import timezone
from django.conf import settings

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        
        return self.body[:100]
    
    
    
   
    
    


# Create your models here.
