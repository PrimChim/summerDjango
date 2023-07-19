from django.urls import path
from .views import index, about, create, contacts,partData

urlpatterns = [
    path('',index, name='index'),
    path('about/',about, name='about'),
    path('create/',create, name='create'),
    path('<int:id>',partData),
    path('contacts/',contacts, name='contacts'),
]