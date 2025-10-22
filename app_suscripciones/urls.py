from django.urls import path
from . import views

app_name = 'app_suscripciones'

urlpatterns = [
    # URLs para Usuarios
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('usuario/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('editar-usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('borrar-usuario/<int:usuario_id>/', views.borrar_usuario, name='borrar_usuario'),
    
    # URLs para Planes
    path('planes/', views.listar_planes, name='listar_planes'),
    path('plan/<int:plan_id>/', views.detalle_plan, name='detalle_plan'),
    path('crear-plan/', views.crear_plan, name='crear_plan'),
    path('editar-plan/<int:plan_id>/', views.editar_plan, name='editar_plan'),
    path('borrar-plan/<int:plan_id>/', views.borrar_plan, name='borrar_plan'),
]