from django.urls import path
from .views import index, about, create, contacts,partData, delete, update

urlpatterns = [
    path('',index, name='index'),
    path('about/',about, name='about'),
    path('create/',create, name='create'),
    path('<int:id>',partData,name='particular'),
    path('contacts/',contacts, name='contacts'),
    path('delete/<int:id>',delete,name='delete'),
    path('update/<int:id>',update,name='update'),
]