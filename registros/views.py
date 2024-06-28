from django.shortcuts import render, redirect

from registros.forms import UsuarioForm, UsuarioEditarForm
from registros.models import Usuario

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages


from PIL import Image
# Create your views here.
def usuario_list_view(request, id=None):
    titulo = "Usuarios"
    
    if request.method == 'POST' and id:
        usuario = Usuario.objects.get(id=id)
        form = UsuarioEditarForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            usuario= form.save()
            messages.success(request, f'¡El usuario se edito de forma exitosa')
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