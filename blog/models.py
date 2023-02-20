from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='blog/images', null=True, blank=True)

    def __str__(self):
        return self.title