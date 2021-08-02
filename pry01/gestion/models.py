from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Trabajador(models.Model):
    dni=models.CharField(max_length=8, primary_key=True)
    nombre=models.CharField(max_length=50,null=False)
    apellido=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=100,null=True)
    telefono=models.CharField(max_length=11,null=False)
    direccion=models.CharField(max_length=100, null=False)
    rol=models.CharField(max_length=2, null=True)

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,password=None):
        if not email:
            raise ValueError('El usuario debe de tener correo electrónico')
        
        usuario=self.model(
            username=username, 
            email=self.normalize_email(email), 
            nombres=nombres, 
            apellidos=apellidos,
            )
    
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self,email,username,nombres,apellidos,password):
        usuario=self.create_user(
            email,
            username=username,  
            nombres=nombres, 
            apellidos=apellidos,
            password=password
        )
        usuario.usuario_administrador= True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    username=models.CharField(unique=True, max_length=100)
    email=models.EmailField(max_length=100,null=True)
    nombres=models.CharField(max_length=50,null=False)
    apellidos=models.CharField(max_length=50,null=False)
    usuario_activo=models.BooleanField(default=True)
    usuario_administrador=models.BooleanField(default=False)
    dni_trabajador=models.ForeignKey('Trabajador',on_delete=models.DO_NOTHING, null=True)
    objects=UsuarioManager()

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['nombres','apellidos','email']

    def __str__(self):
        return f'Usuario {self.nombres}, {self.apellidos}'
    
    def has_perm(self,perm,ob = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador



class Proveedor(models.Model):
    ruc=models.CharField(primary_key=True,max_length=11)
    razon_social=models.CharField(max_length=50, null=False)
    contacto=models.CharField(max_length=100, null=False)
    telefono_contacto=models.CharField(max_length=9,null=False)
    email=models.EmailField(max_length=100,null=True, unique=True)
    direccion=models.CharField(max_length=70,null=False)
    telefono_proveedor=models.CharField(max_length=9,null=False)

class Cliente(models.Model):
    dni_cliente=models.CharField(max_length=11, primary_key=True)
    nombre=models.CharField(max_length=50,null=False)
    apellido=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=100,null=True)
    telefono=models.CharField(max_length=11,null=False)
    direccion=models.CharField(max_length=100, null=False)

class Tipo_Documento(models.Model):
    id_TipoDocumento=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=20,null=False, unique=True)

class Forma_Pago(models.Model):
    id_FormaPago=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=20,null=False, unique=True)

class Lote(models.Model):
    id_Lote=models.AutoField(primary_key=True) 
    descripcion=models.CharField(max_length=10,null=False, unique=True)

class Unidad_Medida(models.Model):
    id_UnidadMedida=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=10,null=False, unique=True)

class Laboratorio(models.Model):
    ruc_laboratorio=models.CharField(max_length=11, primary_key=True)
    razon_social=models.CharField(max_length=50, null=False)
    direccion=models.CharField(max_length=80, null=False)
    telefono=models.CharField(max_length=9,null=False)

class Caja(models.Model):
    id_caja=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=15,null=False, unique=True)

class Medicamento(models.Model):
    codigo_medicamento=models.CharField(max_length=10, primary_key=True)
    descripcion=models.CharField(max_length=20, null=False)
    accion_farm=models.CharField(max_length=100, null=False)
    stock_minimo=models.IntegerField(null=False)
    fecha_vencimiento=models.DateField(null=False)
    precio=models.DecimalField(max_digits=8, decimal_places=2,null=True)
    stock=models.IntegerField(null=False)
    estado=models.BooleanField(null=False)
    ruc_laboratorio=models.ForeignKey('Laboratorio',on_delete=models.DO_NOTHING)
    id_unidad_medida=models.ForeignKey('Unidad_Medida',on_delete=models.DO_NOTHING)

class Compra(models.Model):
    id_Compra=models.AutoField(primary_key=True)
    serie_comprobante=models.CharField(max_length=4,null=True)#pk
    numero_comprobante=models.CharField(max_length=8,null=True)#pk
    id_TipoDocumento=models.ForeignKey('Tipo_Documento',on_delete=models.DO_NOTHING) #pk foranea tipo_documento
    monto_compra=models.DecimalField(max_digits=10, decimal_places=2, null=False)
    fechaCompra=models.DateField(null=False)
    ruc_proveedor=models.ForeignKey('Proveedor',on_delete=models.DO_NOTHING) # pk foranea proveedor
    estado=models.BooleanField(null=False)
    dni=models.ForeignKey('Trabajador',on_delete=models.DO_NOTHING)

class Detalle_Compra(models.Model):
    id_DetalleCompra=models.AutoField(primary_key=True)
    id_Compra=models.ForeignKey('Compra',on_delete=models.DO_NOTHING)
    id_Lote=models.ForeignKey('Lote',on_delete=models.DO_NOTHING)
    codigo_medicamento=models.ForeignKey('Medicamento',on_delete=models.DO_NOTHING)# pk foranea producto
    precio=models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cantidad=models.IntegerField(null=False)
    ruc_proveedor=models.ForeignKey('Proveedor',on_delete=models.DO_NOTHING)

class Venta(models.Model):
    id_Venta=models.AutoField(primary_key=True)
    serie_comprobante= models.CharField(max_length=4) #pk
    numero_comprobante= models.CharField(max_length=4) #pk
    id_TipoDocumento=models.ForeignKey('Tipo_Documento',on_delete=models.DO_NOTHING) #foranea tipo_documento #pk
    monto=models.DecimalField(max_digits=8, decimal_places=2,null=False)
    fechaVenta=models.DateField(null=False)
    id_FormaPago=models.ForeignKey('Forma_Pago',on_delete=models.DO_NOTHING) #foranea forma_pago
    dni_Cliente=models.ForeignKey('Cliente',on_delete=models.DO_NOTHING) #foranea cliente
    dni=models.ForeignKey('Trabajador',on_delete=models.DO_NOTHING) #foranea trabajador
    estado=models.BooleanField(null=False)
    id_caja=models.ForeignKey('Caja',on_delete=models.DO_NOTHING)

   

class Detalle_Venta(models.Model):
    id_DetalleVenta=models.AutoField(primary_key=True)
    id_Venta=models.ForeignKey('Venta',on_delete=models.DO_NOTHING)
    precio=models.DecimalField(max_digits=8, decimal_places=2, null=False)
    cantidad=models.IntegerField(null=False)
    codigo_medicamento=models.ForeignKey('Medicamento',on_delete=models.DO_NOTHING)#PK foranea producto

    




