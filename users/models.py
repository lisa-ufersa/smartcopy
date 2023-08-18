from django.db import models
from django.contrib.auth.models import User

from unidades.models import Unidade

# Create your models here.

class UserProfileExample(models.Model):

    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class Fiscal(models.Model):
    matricula = models.IntegerField()
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="fiscal")
    data_vinculo = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Fiscal"
        verbose_name_plural = "Fiscais"

    def __str__(self):
        return self.user.username

class Requisitante(models.Model):
    matricula = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Requisitante"
        verbose_name_plural = "Requisitantes"

    def __str__(self):
        return self.user.username
    
class Xerox(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="xerox")
    cnpj = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Responsavel"
        verbose_name_plural = "Responsaveis"

    def __str__(self):
        return self.user.username