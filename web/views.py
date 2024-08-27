from django.shortcuts import render
from web.models import flan

# Create your views here.
def index(request):
    flanes = flan.objects.all()
    flanes_privados = flan.objects.filter(is_private=True)
    flanes_publicos = flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes,
        'flanes_privados': flanes_privados,
        'flanes_publicos': flanes_publicos
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

def welcome(request):   
    return render(request, 'welcome.html')