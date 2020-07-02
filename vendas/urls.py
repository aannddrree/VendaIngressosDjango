from django.urls import path
from .views import menu, list_torcedor, create_torcedor, update_torcedor, delete_torcedor, list_ingresso\
    , create_ingresso, update_ingresso, delete_ingresso, list_compra, create_compra

urlpatterns = [
    path('', menu, name='menu'),
    path('torcedor/', list_torcedor, name='list_torcedor'),
    path('ingresso/', list_ingresso, name='list_ingresso'),
    path('compra/', list_compra, name='list_compra'),
    path('torcedor/new', create_torcedor, name='create_torcedor'),
    path('ingresso/new', create_ingresso, name='create_ingresso'),
    path('compra/new', create_compra, name='create_compra'),
    path('torcedor/update/<int:id>/', update_torcedor, name='update_torcedor'),
    path('ingresso/update/<int:id>/', update_ingresso, name='update_ingresso'),
    path('torcedor/delete/<int:id>/', delete_torcedor, name='delete_torcedor'),
    path('ingresso/delete/<int:id>/', delete_ingresso, name='delete_ingresso'),
]
