from django.db import models

class Photo(models.Model):
    choices = [('Professional', 'Professional'), ('Photography', 'Photography'),]
    image = models.ImageField(upload_to='photos')
    category = models.CharField(max_length=20, choices=choices, default='Photography')
    description = models.TextField(default='Hello world!')
    title = models.CharField(max_length=50, default='Hello world!')
    def __str__(self):
        return self.title