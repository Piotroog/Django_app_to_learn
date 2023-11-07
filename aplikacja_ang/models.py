from django.db import models

from django.contrib.auth.models import User


from django.dispatch import receiver
from django.db.models.signals import post_save


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

@receiver(post_save, sender=User, dispatch_uid="new user")
def Funkcja(sender, instance, created, raw, using, **kwargs):
    if created:
        for i in Slowko.objects.all():
            ZnajomoscSlowka.objects.create(slowko=i, user = instance)
