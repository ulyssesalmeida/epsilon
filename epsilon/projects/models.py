from django.db import models
from django.utils.translation import ugettext as _
from datetime import date

# Create your models here.
class Pip(models.Model):
    class Meta:
        ordering = ['pipId']
        
    pipId = models.CharField(_('Id'), max_length=8, unique=True)
    title = models.CharField(_('Título'), max_length=90, unique=True)
    orgUnit = models.CharField(_('Unidade Solicitante'), max_length=10)
    client = models.CharField(_('Cliente'), max_length=30)
    justification = models.TextField(_('Justificativa'))
    objectives = models.TextField(_('Objetivos'))
    cost_estimates = models.CharField(_('Estimativa de Gastos'), max_length=60)

    def __get_next_pipId(self):
        q = Pip.objects.filter(pipId__startswith='P{}'.format(date.today().year))
        proposals_this_year = q.count()
        return "P{}{:03d}".format(date.today().year, proposals_this_year+1)

    def save(self, *args, **kwargs):
        if not self.pipId:
            self.pipId = self.__get_next_pipId()
        super().save(*args, **kwargs)