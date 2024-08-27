from django.shortcuts import render
from web.models import flan

# Create your views here.
def index(request):
    flanes_publicos = flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes_publicos
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

def welcome(request):
    flanes_privados = flan.objects.filter(is_private=True)
    context = {
        'flanes': flanes_privados
    }
    return render(request, 'welcome.html', context)