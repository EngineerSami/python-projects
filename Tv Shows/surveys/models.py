from django.db import models
class ShowManager(models.Manager):
    def basic_validator(self, postData, show=None):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['description']) < 10:
            errors["description"] = "description should be at least 10 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
            
        return errors
    
    
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    objects = ShowManager() 
    
