from django.db import models

# Create your models here.

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published')
    tutorial_links = models.TextField()

    def __str__(self):
        return self.tutorial_title

class cars(models.Model):
    car_name = models.CharField(max_length=200)
    car_description = models.TextField()
    car_age = models.DateTimeField('date built')

    def __str__(self):
        return self.car_name
