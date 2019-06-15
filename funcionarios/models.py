from django.db import models
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)