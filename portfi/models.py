from django.db import models

class Project(models.Model):
    Title = models.CharField(max_length=200)
    Pic = models.ImageField(upload_to='images')
    Description = models.TextField()
    git = models.URLField(blank=True)
    utube = models.URLField(blank=True)

    def __str__(self):
        return self.Title

class Certificates(models.Model):
    pic = models.ImageField(upload_to='images')

