from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio-sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('mis-residuos/', views.mis_residuos, name='mis_residuos'),
    path('registrar-residuo/', views.registrar_residuo, name='registrar_residuo'),
    path('registro-usuario/', views.registro_usuario, name='registro_usuario'),
    path('exito/', views.exito, name='exito'),
    path('encuesta/', views.encuesta, name='encuesta'),
    path('encuesta-enviada/', views.encuesta_enviada, name='encuesta_enviada'),
    path('informacion/', views.informacion, name='informacion'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)