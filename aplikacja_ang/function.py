from .models import Slowko, ZnajomoscSlowka, User
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User, dispatch_uid="new user")
def Funkcja(sender, instance, created, raw, using, **kwargs):
    for i in Slowko.object.all():
        ZnajomoscSlowka.objects.create(slowko=i, user = instance)
