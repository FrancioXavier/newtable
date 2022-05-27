from django.shortcuts import render

from .models import Cliente

# Create your views here.


def home(request):
    clientes = Cliente.objects.all().order_by('-id')
    return render(request, 'table/pages/home.html', context={
        'clientes': clientes,
    })
