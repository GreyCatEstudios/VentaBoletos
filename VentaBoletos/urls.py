from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('u/', include('usuarios.urls')),
    path('e/', include('eventos.urls')),
    path('b/', include('boletos.urls')),
]
