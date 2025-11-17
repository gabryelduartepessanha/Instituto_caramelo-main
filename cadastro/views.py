from django.shortcuts import render, redirect
from .models import ONG, Parceiro


def index(request):
    return render(request, 'index.html')


def cadastro_sucesso(request):
    return render(request, 'sucesso.html')


def registrar_ong(request):
    mensagem = None  # Variável para enviar feedback ao template

    if request.method == "POST":
        # Pegando dados do formulário
        nome = request.POST.get('nome')
        cidade = request.POST.get('cidade')
        representante = request.POST.get('representante')
        email = request.POST.get('email')
        cnpj = request.POST.get('cnpj')  # Agora minúsculo, igual ao model
        motivacao = request.POST.get('motivacao')

        # Verificando se todos os campos obrigatórios foram preenchidos
        if not nome or not cnpj:
            mensagem = "Nome e CNPJ são obrigatórios."
        else:
            # Tentando criar a ONG no banco
            try:
                ong = ONG.objects.create(
                    nome=nome,
                    cidade=cidade,
                    representante=representante,
                    email=email,
                    cnpj=cnpj,
                    motivacao=motivacao
                )
                mensagem = "ONG cadastrada com sucesso!"
                # Limpar campos após cadastro
                return render(request, 'seu_template.html', {'mensagem': mensagem})
            except Exception as e:
                # Se já existir o CNPJ ou outro erro
                mensagem = f"Erro ao cadastrar ONG: {str(e)}"

    return render(request, 'seu_template.html', {'mensagem': mensagem})


def ongs_rejeitadas(request):
    rejeitadas = ONG.objects.filter(status="rejeitada")
    return render(request, "ongs_rejeitadas.html", {"ongs": rejeitadas})


def parceiros(request):
    parceiros = Parceiro.objects.filter(aprovado=True)
    return render(request, "parceiros.html", {"parceiros": parceiros})
