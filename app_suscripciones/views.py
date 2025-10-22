from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario, PlanSuscripcion
from .forms import UsuarioForm, PlanSuscripcionForm

# Vistas para Usuarios
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def detalle_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'detalle_usuario.html', {'usuario': usuario})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_suscripciones:listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'formulario_usuario.html', {'form': form, 'titulo': 'Crear Usuario'})

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('app_suscripciones:detalle_usuario', usuario_id=usuario.id)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'formulario_usuario.html', {'form': form, 'titulo': 'Editar Usuario'})

def borrar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('app_suscripciones:listar_usuarios')
    return render(request, 'confirmar_borrar.html', {'usuario': usuario})

# Vistas para Planes de Suscripción
def listar_planes(request):
    planes = PlanSuscripcion.objects.all()
    return render(request, 'listar_planes.html', {'planes': planes})

def detalle_plan(request, plan_id):
    plan = get_object_or_404(PlanSuscripcion, id=plan_id)
    usuarios_con_plan = Usuario.objects.filter(plan=plan)
    return render(request, 'detalle_plan.html', {'plan': plan, 'usuarios_con_plan': usuarios_con_plan})

def crear_plan(request):
    if request.method == 'POST':
        form = PlanSuscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_suscripciones:listar_planes')
    else:
        form = PlanSuscripcionForm()
    return render(request, 'formulario_plan.html', {'form': form, 'titulo': 'Crear Plan'})

def editar_plan(request, plan_id):
    plan = get_object_or_404(PlanSuscripcion, id=plan_id)
    if request.method == 'POST':
        form = PlanSuscripcionForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('app_suscripciones:detalle_plan', plan_id=plan.id)
    else:
        form = PlanSuscripcionForm(instance=plan)
    return render(request, 'formulario_plan.html', {'form': form, 'titulo': 'Editar Plan'})

def borrar_plan(request, plan_id):
    plan = get_object_or_404(PlanSuscripcion, id=plan_id)
    if request.method == 'POST':
        plan.delete()
        return redirect('app_suscripciones:listar_planes')
    return render(request, 'confirmar_borrar_plan.html', {'plan': plan})