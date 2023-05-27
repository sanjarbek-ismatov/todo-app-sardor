from django.db import models
from django.urls import reverse


# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.date}'

    def get_absolute_url(self):
        return reverse('home')
