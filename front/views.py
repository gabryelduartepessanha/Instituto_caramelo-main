from django.shortcuts import render, redirect
from cadastro.models import ONG, Parceiro


def registrar_ong(request):
    mensagem = None

    if request.method == "POST":
        nome = request.POST.get("nome")
        cidade = request.POST.get("cidade")
        representante = request.POST.get("representante")
        cnpj = request.POST.get("cnpj")
        motivacao = request.POST.get("motivacao")
        email = request.POST.get("email")

        ONG.objects.create(
            nome=nome,
            cidade=cidade,
            representante=representante,
            cnpj=cnpj,
            motivacao=motivacao,
            email=email,
            status="pendente"
        )

        mensagem = "Cadastrado com sucesso! Aguarde o resultado."

    return render(request, "index.html", {"mensagem": mensagem})


def index(request):
    return render(request, "index.html")


def parceiros(request):
    parceiros = Parceiro.objects.filter(aprovado=True)
    if not parceiros:
        mensagem = "Nenhum parceiro aprovado no momento."
    else:
        mensagem = None
    return render(request, 'parceiros.html', {'parceiros': parceiros, 'mensagem': mensagem})


def quem_somos(request):
    return render(request, 'quemsomos_index.html')
