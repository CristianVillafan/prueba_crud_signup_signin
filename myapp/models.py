from django.db import models
from django.contrib.auth.models import User

skin_style = [
    ('Normal','Normal'),
    ('Original','Original'),
    ('Anime','Anime'),

]
# Create your models here.
class Orders(models.Model):
    name=models.CharField(max_length=100)
    skinstyle=models.CharField(max_length=50 ,null=False, blank=False, choices=skin_style, default='Original')
    size=models.FloatField(blank=True, null=True, help_text='cm', default=0)
    units=models.IntegerField(null=True, blank=True, default=1, help_text='Cantidad de unidades')
    description=models.TextField(blank=True, help_text='Especifica detalles o modificaciones especiales no especificados anteriormente')
    status=models.CharField(max_length=100, default='En espera...', blank=True)
    price=models.IntegerField(null=True, default=None)
    create=models.DateTimeField(auto_now=True)
    datecomplete=models.DateTimeField(null=True, blank=True)
    urgency=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + ' - by ' + self.user.username

