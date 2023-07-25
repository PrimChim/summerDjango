from django.contrib import admin
from django.urls import path, include
from demo.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('migrations.urls'))
]
