from django.forms import ValidationError
from django.shortcuts import render, redirect

from registros.forms import LoginForm, UserRegisterForm, UsuarioForm, UsuarioEditarForm, PerfilForm
from registros.models import Usuario

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode


from PIL import Image
# Create your views here.
def usuario_list_view(request, id=None):
    titulo = "Usuarios"
    
    if request.method == 'POST' and id:
        usuario = Usuario.objects.get(id=id)
        form = UsuarioEditarForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            usuario= form.save()
            messages.success(request, f'¡El usuario se editó de forma exitosa')
            return redirect("usuarios-listar")
        else:
            form= UsuarioEditarForm(request.POST, request.FILES, instance=usuario)
            messages.error(request, f'Error al editar el usuario')
            
    elif request.method == 'POST':
        form= UsuarioForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=request.POST.get('documento')).exists():
                user= User.objects.create_user('nombre', 'email@gmail', 'password')
                user.username= request.POST.get('documento')
                user.first_name= request.POST.get('primer_nombre')
                user.last_name= request.POST.get('primer_apellido')
                user.email= request.POST.get('correo')
                user.password= make_password("@" + request.POST['primer_nombre'][0] + request.POST['primer_apellido'][0] + request.POST['documento'][-4:])
                user.save()
            else:
                user= User.objects.get(username=request.POST.get('documento'))
            usuario= Usuario.objects.create(
                primer_nombre= request.POST.get('primer_nombre'),
                segundo_nombre= request.POST.get('segundo_nombre'),
                primer_apellido= request.POST.get('primer_apellido'),
                segundo_apellido= request.POST.get('segundo_apellido'),
                fecha_nacimiento= request.POST.get('fecha_nacimiento'),
                imagen= request.FILES.get('imagen'),
                correo= request.POST.get('correo'),
                tipo_documento= request.POST.get('tipo_documento'),
                documento= request.POST.get('documento'),
                user= user
            )
            if usuario.imagen:
                img= Image.open(usuario.imagen.path)
                img= img.resize((500,500))
                img.save(usuario.imagen.path)
            usuario.save()
            messages.success(request, f'¡El Usuario se agregó de forma exitosa!')
            return redirect('usuarios-listar')
        else:
            form= UsuarioForm(request.POST, request.FILES)
            messages.error(request, f'¡Error al cargar el usuario!')
    else:
        if(id):
            usuario = Usuario.objects.get(id=id)
            form = UsuarioEditarForm(instance=usuario)
        else:
            form= UsuarioForm()
    context = {
        "titulo": titulo,
        "form": form,
    }
    return render(request, 'admin/registros/usuarios.html', context)

def usuario_delete_view(request, id):
    usuario = Usuario.objects.filter(id=id)
    usuario.update(estado=False)
    return redirect('usuarios-listar')

def header_register(request):
    return render(request, 'users/registrados/registrado_header.html')

def add_products(request):
    return render(request, 'admin/add_products/add_producto.html')

def perfil(request):
    return render(request, 'users/perfil/perfil-usuario.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Ahora puede iniciar sesión')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register-login/register.html', {'form': form})

def login_view(request):
    next = request.GET.get('next', 'index-user')  # Cambia 'home' por la URL por el html principal
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(next)
            else:
                form.add_error(None, 'Correo o contraseña incorrectos.')
    else:
        form = LoginForm()
    
    return render(request, 'users/register-login/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index-user')

def send_password_reset_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = get_user_model().objects.filter(email__iexact=email).first()
        if user:
            uidb64 = urlsafe_base64_encode(user.pk)
            token = default_token_generator.generate_token(user)
            url = f'http://localhost:8000/password-reset/confirm/{uidb64}/{token}'
            send_mail(
                'Recuperación de contraseña',
                f'Para restablecer tu contraseña, haz clic en el siguiente enlace: {url}',
                'tu_correo@example.com',
                [email],
                fail_silently=False
            )
            messages.success(request, 'Te hemos enviado un correo electrónico con instrucciones para restablecer tu contraseña.')
        else:
            messages.error(request, 'No encontramos una cuenta asociada a ese correo electrónico.')
    return render(request, 'users/register-login/password_reset_form.html')

def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, ValidationError):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        return redirect('password_reset_change', uidb64=uidb64, token=token)
    else:
        messages.error(request, 'El enlace de recuperación de contraseña no es válido.')
        return render(request, 'users/register-login/password_reset_confirm.html')
    
def actualizar_perfil(request): 
    titulo = "Perfil" 
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        cedula = request.POST.get('cedula')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        genero = request.POST.get('genero')

        # Actualizar los datos del usuario
        user = request.user  # Usuario autenticado
        user.first_name = nombre
        user.last_name = apellido
        user.profile.fecha_nacimiento = fecha_nacimiento
        user.profile.cedula = cedula
        user.email = email
        user.profile.telefono = telefono
        user.profile.genero = genero
        user.save()

        messages.success(request, '¡Perfil actualizado correctamente!')
        return redirect('partials/user/user_profile.html/')  # Redirige a la página de perfil o a donde desees
        # Si no es una solicitud POST, simplemente renderiza el template
    form= PerfilForm()
    context = {
        "titulo": titulo,
        "form": form,
    }
    
    return render(request, 'users/perfil/user_profile.html', context)

def procesar_pago(request):
    if request.method == 'POST':
        # Obtener los datos del formulario de pago
        nombre = request.POST['nombre']
        numero_tarjeta = request.POST['numero_tarjeta']
        # Lógica para procesar el pago
        # ...
        return redirect('confirmacion_pago')
    else:
        return render(request, 'pago.html')