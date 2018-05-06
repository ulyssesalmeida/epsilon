from django.shortcuts import render, redirect
from django.views.generic import View
from epsilon.projects.forms import PipForm
from epsilon.projects.models import Pip

# Create your views here.

class PipView(View):
    def get(self, request):
        return render(request,
            template_name = "projects/pip_form.html",
            context = {'form':PipForm()})

    def post(self, request):
        form = PipForm(request.POST)
        if not form.is_valid():
            return render(request,
                template_name = "projects/pip_form.html",
                context = {'form':form})
        obj = form.save()
        return redirect('/projetos/pip/{}'.format(obj.pipId))
