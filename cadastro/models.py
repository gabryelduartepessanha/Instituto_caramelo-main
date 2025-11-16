from django.db import models


class ONG(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("aprovada", "Aprovada"),
        ("rejeitada", "Rejeitada"),
    ]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pendente')
    nome = models.CharField(max_length=200)
    cidade = models.CharField(max_length=120, blank=True, null=True)
    representante = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cnpj = models.CharField(max_length=18, unique=True)
    motivacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Parceiro(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    representante = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    motivacao = models.TextField()
    aprovado = models.BooleanField(default=False)

    ong = models.ForeignKey(ONG, on_delete=models.CASCADE,
                            related_name='parceiros', null=True, blank=True)

    def __str__(self):
        return self.nome


class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    aprovado = models.BooleanField(default=False)
