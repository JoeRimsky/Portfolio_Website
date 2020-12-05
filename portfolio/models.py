from django.db import models

class Photo(models.Model):
    choices = [('Professional', 'Professional'), ('Photography', 'Photography'),]
    image = models.ImageField(upload_to='photos')
    category = models.CharField(max_length=20, choices=choices, default='Photography')