from django.db import models

class PlanSuscripcion(models.Model):
    nombre_plan = models.CharField(max_length=50)
    precio_mensual = models.DecimalField(max_digits=6, decimal_places=2)
    dispositivos_simultaneos = models.IntegerField()
    descargas_offline = models.BooleanField()
    anuncios = models.BooleanField()

    def __str__(self):
        return self.nombre_plan

    class Meta:
        verbose_name = "Plan de Suscripción"
        verbose_name_plural = "Planes de Suscripción"

class Usuario(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    
    email = models.EmailField(unique=True, max_length=150)
    fecha_registro = models.DateField()
    pais = models.CharField(max_length=50)
    plan = models.ForeignKey(PlanSuscripcion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Activo')
    foto_de_perfil = models.ImageField(upload_to='img_usuarios/', blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"