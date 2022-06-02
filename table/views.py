from django.shortcuts import get_object_or_404, render

from .models import Cliente

# Create your views here.


def home(request):
    clientes = Cliente.objects.all().order_by('-id')
    return render(request, 'table/pages/home.html', context={
        'clientes': clientes,
    })


def cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)

    return render(request, 'table/pages/cliente-view.html', context={
        'cliente': cliente,
    })
