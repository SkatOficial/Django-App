from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("autosDelMarApp.urls")),
    path('autenticacion/', include("autenticacion.urls")),
    path('verVehículos/', include("autos.urls"))
]
