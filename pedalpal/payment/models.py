from django.db import models
from authentication.models import Profile


class Payment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user + " " + self.amount)
