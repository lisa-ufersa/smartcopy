from django.db import models

# Create your models here.

class Maquina(models.Model):
    modelo = models.CharField(max_length=140)
    ultima_manutencao = models.DateField()
    capacidade = models.IntegerField()
    is_active = models.BooleanField()


    class Meta:
        verbose_name = "Máquina"
        verbose_name_plural = "Máquinas"

    def __str__(self):
        return self.modelo

class Unidade(models.Model):
    local = models.CharField(max_length=140)
    maquina = models.ManyToManyField(Maquina)
    is_active = models.BooleanField()


    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"

    def __str__(self):
        return self.local

class Impressao(models.Model):
    qnt = models.IntegerField()
    colorido = models.BooleanField()
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    data_solicitada = models.DateField()
    data_imperssa = models.DateField()
    data_entregue = models.DateField()
    arquivo = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Impressão"
        verbose_name_plural = "Impressões"
    
    def __str__(self):
        return f"{self.requisitante.user.username} | {self.data_solicitada} | {self.arquivo}"