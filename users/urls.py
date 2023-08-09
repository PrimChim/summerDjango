from django.urls import path,include
from .views import registerUser,loginUser,logoutUser

app_name = 'users'
urlpatterns = [
    path('register/', registerUser, name='register'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
]