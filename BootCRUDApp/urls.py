from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editItem/<int:itemID>', views.editItem, name='editItem'),

]