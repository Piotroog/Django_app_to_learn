from django.db import models

from django.contrib.auth.models import User

class Slowko(models.Model):
    polskie = models.CharField(max_length=100)
    angielskie = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.polskie} - {self.angielskie}"

class ZnajomoscSlowka(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slowko = models.ForeignKey(Slowko, on_delete=models.CASCADE)
    zna = models.BooleanField(default=False)

    class Meta:
        unique_together = [['user', 'slowko']]

