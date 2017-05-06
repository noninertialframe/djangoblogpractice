from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=150)
    text = models.TextField(null=False, blank=False)
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-published_date', '-pk', )
        
    def __str__(self):
        return self.title
    

