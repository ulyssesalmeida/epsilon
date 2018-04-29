from django.shortcuts import render
from epsilon.projects.forms import PipForm

# Create your views here.
def pip(request):
    return render(request,
        template_name = "projects/pip_form.html",
        context = {'form':PipForm()})