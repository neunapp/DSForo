from django.db import models
from django.db.models import Count, Max
from django.contrib.postgres.search import TrigramSimilarity

class EntryManager(models.Manager):
    """procedimiento para cancha"""

    def search_entry(self, name):
        """funcion que busca entradas"""

        #verificamos si nombre tiene mas de 3 digitos
        if len(name) > 3:
            #filtramos por nombre
            consulta = self.filter(
                anulate=False,
                title__trigram_similar=name,
            ).order_by('-vists')[:20]
            return consulta
        else:
            return self.filter(
                anulate=False,
                title__icontains=name,
            ).order_by('-vists')[:20]
