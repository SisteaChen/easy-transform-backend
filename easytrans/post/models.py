from django.db import models

# Create your models here.
class Poster(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=10000, default="no content now")
    date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title