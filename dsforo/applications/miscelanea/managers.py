from django.db import models
from django.db.models import Count, Max, F, Q, When
from django.contrib.postgres.search import TrigramSimilarity


class CategoryManager(models.Manager):
    """procedimiento para Categoria"""

    def category_temas(self):
        """ Lista todas las categorias con sus conjuto de temas"""
        consulta = self.filter()
        return consulta
