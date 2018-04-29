from django.shortcuts import render

# Create your views here.
def pip(request):
    return render(request, "projects/pip_form.html")