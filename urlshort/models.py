from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class ShortURL(models.Model):
    original_url = models.URLField(max_length=700)
    short_url = models.CharField(max_length=100, unique=True)
    time_date_created = models.DateTimeField(auto_now_add=True)
    click_count = models.IntegerField(default=0)
    # link each url to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # optional expiration time
    expires_at = models.DateTimeField(null=True, blank=True)
    
    def is_expired(self):
        if self.expires_at is None:
            return False
        return timezone.now() > self.expires_at
    
    def __str__(self):
        return self.short_url + " -> " + self.original_url[:50]
    
   