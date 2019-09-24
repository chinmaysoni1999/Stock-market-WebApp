from django.db import models
from django.utils import timezone

class Tickers(models.Model):
    ticker = models.CharField(max_length=10)
    date_posted = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.ticker
