from django.shortcuts import render
from django.views.generic import View
from epsilon.projects.forms import PipForm

# Create your views here.

class PipView(View):
    def get(self, request):
        return render(request,
            template_name = "projects/pip_form.html",
            context = {'form':PipForm()})
