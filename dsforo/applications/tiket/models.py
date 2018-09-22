from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible


class Tiket(TimeStampedModel):
    """
    modelo para tiket de consulta que envie un usuario
    """

    TYPE_TIKET = (
        ('0', 'Problemas Con La Plataforma'),
        ('1', 'Consulta Sobre DeporStart'),
        ('2', 'Otro'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='tiket_creator',
        on_delete=models.CASCADE,
    )
    tipo = models.CharField('Tipo de Tiket', max_length=2, choices=TYPE_TIKET)
    subject = models.CharField('Asunto', max_length=120)
    message = models.TextField('Mensaje')
    anulate = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Tiket'
        verbose_name_plural = 'Tikets'

    def __str__(self):
        return self.subject



class Suggestion(TimeStampedModel):
    """
    modelo para sugerencias sobre la plataforma
    """

    email = models.EmailField()
    fullname = models.CharField('Nombre Completo', blank=True, max_length=150)
    description = models.CharField('Torneo o Equipo', blank=True, max_length=150)
    suggestion = models.TextField('Sugerencia')

    class Meta:
        verbose_name = 'Sugerencia'
        verbose_name_plural = 'Sugerencias'

    def __str__(self):
        return self.email
