from django.shortcuts import render

# Create your views here.
def pip(request):
    return render(request, "pip_form.html")