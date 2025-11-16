from django.shortcuts import render, redirect
from .models import ONG, Parceiro


def index(request):
    return render(request, 'index.html')


def cadastro_sucesso(request):
    return render(request, 'sucesso.html')


def registrar_ong(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        cidade = request.POST.get("cidade")
        representante = request.POST.get("representante")
        cnpj = request.POST.get("cnpj")
        motivacao = request.POST.get("motivacao")

        ONG.objects.create(
            nome=nome,
            cidade=cidade,
            email=email,
            representante=representante,
            cnpj=cnpj,
            motivacao=motivacao,
        )

        return redirect("cadastro_sucesso")

    return redirect("index")


def ongs_aprovadas(request):
    aprovadas = ONG.objects.filter(status="aprovada")
    return render(request, "ongs_aprovadas.html", {"ongs": aprovadas})


def ongs_rejeitadas(request):
    rejeitadas = ONG.objects.filter(status="rejeitada")
    return render(request, "ongs_rejeitadas.html", {"ongs": rejeitadas})


def parceiros(request):
    parceiros = Parceiro.objects.filter(aprovado=True)
    return render(request, "parceiros.html", {"parceiros": parceiros})
