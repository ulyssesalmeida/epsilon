from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Pip(models.Model):
    title = models.CharField(_('Título'), max_length=90, unique=True)
    orgUnit = models.CharField(_('Unidade Solicitante'), max_length=10)
    client = models.CharField(_('Cliente'), max_length=30)
    justification = models.TextField(_('Justificativa'))
    objectives = models.TextField(_('Objetivos'))
    cost_estimates = models.CharField(_('Estimativa de Gastos'), max_length=60)