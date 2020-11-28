from django.db import models

class MostRecent(models.Model):
    Images = models.ImageField(default="default.jpg",upload_to='pictures')
    foodname = models.CharField(max_length=200)
    prize = models.CharField(max_length=200)

class Feedback(models.Model):
    name = models.CharField(max_length = 100)
    feed = models.CharField(max_length = 200)