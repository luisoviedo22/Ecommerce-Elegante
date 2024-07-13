from django.db import models
from django.contrib.auth.models import User 
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

def get_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.documento}.{ext}"
    return f"registros/usuarios/{filename}"
# Create your models here.

class Usuario(models.Model):
    primer_nombre = models.CharField(max_length=45, verbose_name="Primer Nombre")
    segundo_nombre = models.CharField(max_length=45, verbose_name="Segundo Nombre", blank= True, null= True)
    
    primer_apellido = models.CharField(max_length=45, verbose_name= "Primer Apellido")
    segundo_apellido = models.CharField(max_length=45, verbose_name="Segundo Apellido")
    
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    imagen = models.ImageField(upload_to=get_image_filename, blank=True, null=True, default="registros/usuarios/default-user.jpeg")
    correo = models.EmailField(max_length=50, verbose_name="Correo")
    
    class TipoDocumento(models.TextChoices):
        CEDULA = 'CC', _('Cédula')
        TARJETA = 'TI', _('Tarjeta de Identidad')
        CEDULA_EXTRANJERIA = 'CE', _('Cédula de Extranjería')
    tipo_documento = models.CharField(max_length=2, choices= TipoDocumento.choices, verbose_name="Tipo de Documento")
    documento = models.PositiveIntegerField(verbose_name="Documento", unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    def clean(self):
        self.primer_nombre = self.primer_nombre.title()
    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"
    class Meta:
        verbose_name_plural = "Usuarios"
    @property
    def full_name(self):
        if self.segundo_nombre:
            return f"{self.primer_nombre} {self.segundo_nombre} {self.primer_apellido} {self.segundo_apellido}"
        else:
            return f"{self.primer_nombre} {self.primer_apellido} {self.segundo_apellido}"
    
    def usuario_activo(self):
        if self.estado:
            return Usuario.objects.filter(usuario=self, estado=True)
        else:
            return Usuario.objects.none()
        
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Correo Electrónico', max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Profile(models.Model):
    primer_nombre = models.CharField(max_length=45, verbose_name="Primer Nombre")
    segundo_nombre = models.CharField(max_length=45, verbose_name="Segundo Nombre", blank= True, null= True)
    
    primer_apellido = models.CharField(max_length=45, verbose_name= "Primer Apellido")
    segundo_apellido = models.CharField(max_length=45, verbose_name="Segundo Apellido")
    
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    
    correo = models.EmailField(max_length=50, verbose_name="Correo")
    
    class TipoDocumento(models.TextChoices):
        CEDULA = 'CC', _('Cédula')
        TARJETA = 'TI', _('Tarjeta de Identidad')
        CEDULA_EXTRANJERIA = 'CE', _('Cédula de Extranjería')
    tipo_documento = models.CharField(max_length=2, choices= TipoDocumento.choices, verbose_name="Tipo de Documento")
    documento = models.PositiveIntegerField(verbose_name="Documento", unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    def clean(self):
        self.primer_nombre = self.primer_nombre.title()
    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"
    class Meta:
        verbose_name_plural = "Usuarios"
    @property
    def full_name(self):
        if self.segundo_nombre:
            return f"{self.primer_nombre} {self.segundo_nombre} {self.primer_apellido} {self.segundo_apellido}"
        else:
             return f"{self.primer_nombre} {self.primer_apellido} {self.segundo_apellido}"
    
    def usuario_activo(self):
        if self.estado:
            return Usuario.objects.filter(usuario=self, estado=True)
        else:
            return Usuario.objects.none()
