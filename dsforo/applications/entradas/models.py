from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy, reverse

# standard library
from datetime import timedelta, datetime

# third-party
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

# import apps models
from applications.miscelanea.models import Theme, Tag

from .managers import EntryManager



class Entry(TimeStampedModel):
    """
    modelo para entradas o articulos
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='entry_creator',
        on_delete=models.CASCADE,
    )
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    title = models.CharField('Titulo', max_length=200)
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('contenido')
    comentary = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag)
    vists = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    anulate = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    objects = EntryManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy(
            'entradas_app:entrada_detalle',
            kwargs={
                'slug':self.slug,
            }
        )

    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.title, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)
        super(Entry, self).save(*args, **kwargs)


class Comentary(TimeStampedModel):
    """
    modelo para comentarios de una entrada
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comentary_creator',
        on_delete=models.CASCADE,
    )
    entry = models.ForeignKey(
        Entry,
        related_name='comentary_entry',
        on_delete=models.CASCADE
    )
    content = RichTextUploadingField('contenido')
    calification = models.DecimalField(max_digits=3, decimal_places=1)
    destacado = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return self.entry.title


class News(TimeStampedModel):
    """
    modelo para administrar noticias
    """

    TYPE_STANDARD = 'S'  # ESTANDAR
    TYPE_FRONT = 'F'  # PORTADA
    TYPE_OUTSTANDING = 'O'  # DESTACADO
    TYPE_CHOICES = (
        (TYPE_STANDARD, 'Estandar'),
        (TYPE_FRONT, 'Portada'),
        (TYPE_OUTSTANDING, 'Destacado'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='news_creator',
        on_delete=models.CASCADE,
    )
    type_article = models.CharField(
        'tipo de articulo',
        max_length=2,
        choices=TYPE_CHOICES
    )
    title = models.CharField('Titulo', max_length=200)
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('contenido')
    tag = models.ManyToManyField(Tag)
    vists = models.IntegerField(default=0)
    anulate = models.BooleanField(default=False)
    published = models.BooleanField('publicado', default=False)
    slug = models.SlugField(editable=False, max_length=300)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy(
            'entradas_app:noticias_detalle',
            kwargs={
                'slug':self.slug,
            }
        )

    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.title, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)
        super(News, self).save(*args, **kwargs)
