from django.contrib import admin
from .models import ONG, Parceiro
from django.core.mail import send_mail


@admin.register(ONG)
class ONGAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "representante", "cnpj", "status")
    list_filter = ("status",)
    search_fields = ('nome', 'email')
    actions = ["aprovar_ongs", "rejeitar_ongs"]

    def aprovar_ongs(self, request, queryset):
        for ong in queryset:
            ong.status = "aprovada"
            ong.save()

            Parceiro.objects.create(
                nome=ong.nome,
                cidade=ong.cidade,
                representante=ong.representante,
                cnpj=ong.cnpj,
                motivacao=ong.motivacao,
                aprovado=True,
                ong=ong
            )

            if ong.email:
                subject = "Seu cadastro foi aprovado!"
                message = f"Olá {ong.representante},\n\nSua ONG '{ong.nome}' foi aprovada."
                send_mail(
                    subject,
                    message,
                    'no-reply@institutocaramelo.com',
                    [ong.email],
                    fail_silently=False,
                )

        self.message_user(
            request, "ONG(s) aprovadas com sucesso! E parceiros criados.")

    aprovar_ongs.short_description = "Aprovar ONG selecionadas"

    def rejeitar_ongs(self, request, queryset):
        for ong in queryset:
            ong.status = "rejeitada"
            ong.save()

            if ong.email:
                subject = "Seu cadastro foi rejeitado"
                message = f"Olá {ong.representante},\n\nInfelizmente sua ONG '{ong.nome}' foi rejeitada."
                send_mail(
                    subject,
                    message,
                    'no-reply@institutocaramelo.com',
                    [ong.email],
                    fail_silently=False,
                )

        self.message_user(request, "ONG(s) rejeitadas!")

    rejeitar_ongs.short_description = "Rejeitar ONG selecionadas"
