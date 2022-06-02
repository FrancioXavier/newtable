from django.urls import path

from table import views

app_name = 'table'

urlpatterns = [
    path('', views.home, name='home'),
    path('cliente/<int:id>', views.cliente, name='cliente')
]
