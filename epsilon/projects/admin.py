from django.contrib import admin
from epsilon.projects.models import Pip

# Register your models here.

class PipAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pip, PipAdmin)