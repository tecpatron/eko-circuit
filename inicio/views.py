from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Residuo
from .models import RespuestaEncuesta
from .models import ContadorVisitas

def index(request):
    total_usuarios = User.objects.count()

    contador = ContadorVisitas.objects.first()
    if contador:
        contador.visitas += 1
        contador.save()
    else:
        contador = ContadorVisitas.objects.create(visitas=1)

    return render(request, 'inicio/index.html', {
        'total_usuarios': total_usuarios,
        'visitas': contador.visitas,
    })

def informacion(request):
    return render(request, 'inicio/informacion.html')

def exito(request):
    return render(request, 'inicio/exito.html')

def inicio_sesion(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        contrasena = request.POST.get('contrasena')
        user = authenticate(request, username=nombre_usuario, password=contrasena)

        if user is not None:
            login(request, user)
            return redirect('registrar_residuo')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'inicio/inicio_sesion.html')

@login_required
def mis_residuos(request):
    residuos = Residuo.objects.filter(usuario=request.user)
    return render(request, 'inicio/mis_residuos.html', {'residuos': residuos})

@login_required
def registrar_residuo(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        estado = request.POST.get('estado')
        foto = request.FILES.get('foto')

        Residuo.objects.create(
            usuario=request.user,
            tipo=tipo,
            estado=estado,
            foto=foto
        )
        return render(request, 'inicio/exito.html')
    return render(request, 'inicio/registrar_residuo.html')

def registro_usuario(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        contrasena = request.POST.get('contrasena')
        email = request.POST.get('email')

        if User.objects.filter(username=nombre_usuario).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está en uso.')
        else:
            user = User.objects.create_user(username=nombre_usuario, password=contrasena, email=email)
            user.save()
            messages.success(request, 'Usuario registrado con éxito.')
            return redirect('inicio_sesion')

    return render(request, 'inicio/registro_usuario.html')


@login_required
def encuesta(request):
    if request.method == 'POST':
        # Obtener respuestas del formulario
        respuestas = {}
        for i in range(1, 6):
            valor = request.POST.get(f'pregunta{i}')
            if valor is None:
                # Opcional: manejar error si falta respuesta
                return render(request, 'inicio/encuesta.html', {'error': 'Por favor responde todas las preguntas.'})
            respuestas[f'pregunta{i}'] = int(valor)

        # Guardar en la base de datos
        RespuestaEncuesta.objects.create(
            usuario=request.user,
            pregunta1=respuestas['pregunta1'],
            pregunta2=respuestas['pregunta2'],
            pregunta3=respuestas['pregunta3'],
            pregunta4=respuestas['pregunta4'],
            pregunta5=respuestas['pregunta5']
        )

        return redirect('encuesta_enviada')

    return render(request, 'inicio/encuesta.html')

def encuesta_enviada(request):
    return render(request, 'inicio/encuesta_enviada.html')
