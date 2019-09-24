from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Stocks(models.Model):
    ticker = models.CharField(max_length=10)
    date_posted = models.DateTimeField(default = timezone.now)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.ticker

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
