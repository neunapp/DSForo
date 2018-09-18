from django.db import models
from model_utils.models import TimeStampedModel

#
from applications.miscelanea.models import Tag

# Create your models here.

class Home(TimeStampedModel):
    """
    modelo para pagina de inicio
    """

    titleSeo = models.CharField(max_length=200)
    descriptionSeo = models.CharField(max_length=150)
    email1 = models.EmailField()
    email2 = models.EmailField()
    phone1 = models.CharField(blank=True, max_length=15)
    phone2 = models.CharField(blank=True, max_length=15)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    twiter = models.URLField(blank=True)
    google = models.URLField(blank=True)
    pinteres = models.URLField(blank=True)
    tag = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'

    def __str__(self):
        return self.titleSeo
