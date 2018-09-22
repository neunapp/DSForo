from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from model_utils.models import TimeStampedModel
#
from datetime import datetime, timedelta
#
from .managers import CategoryManager


class Category(TimeStampedModel):
    """
    modelo para categorias principales del foro
    """

    name = models.CharField('Nombre', max_length=100)
    icon = models.CharField('icono', max_length=30)

    objects = CategoryManager()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Theme(TimeStampedModel):
    """
    modelo para los temas que pertenecen a un categoria
    """

    TIPO_CHOICES = (
        ('0', 'Usuario'),
        ('1', 'Colaboracion'),
        ('2', 'Administracion'),
    )

    category = models.ForeignKey(Category, related_name="themes", on_delete=models.CASCADE)
    seoName = models.CharField('Titulo para SEO', max_length=120)
    title = models.CharField('Titulo', max_length=100)
    description = models.TextField('Descripcion', blank=True)
    tipo = models.CharField('Tipo de Tema', max_length=2, choices=TIPO_CHOICES)
    icon = models.CharField('class icono', blank=True, max_length=30)
    vists = models.IntegerField(default=0)
    slug = models.SlugField(editable=False, max_length=300)

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.title

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
            slug_unique = '%s %s' % (self.seoName, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.seoName, str(seconds))

        self.slug = slugify(slug_unique)
        super(Theme, self).save(*args, **kwargs)


class Tag(TimeStampedModel):
    """
    modelo para etiquetas SEO
    """

    tag = models.CharField(blank=True, max_length=150)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __str__(self):
        return self.tag
