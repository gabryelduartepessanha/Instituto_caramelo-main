from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import ONG


@receiver(pre_save, sender=ONG)
def armazenar_status_antigo(sender, instance, **kwargs):
    if instance.pk:
        instance._status_antigo = ONG.objects.get(pk=instance.pk).status
    else:
        instance._status_antigo = None


@receiver(post_save, sender=ONG)
def enviar_email_status(sender, instance, created, **kwargs):
    if not instance.email:
        return

    if hasattr(instance, "_status_antigo") and instance._status_antigo == instance.status and instance._status_antigo is not None:
        return

    if created:
        subject = "Cadastro recebido"
        message = (
            f"Olá {instance.representante},\n\n"
            f"Recebemos seu cadastro da ONG '{instance.nome}'. "
            "Logo mais entraremos em contato para mais informações."
        )
    elif instance.status == "aprovada":
        subject = "Seu cadastro foi aprovado!"
        message = f"Olá {instance.representante},\n\nSua ONG '{instance.nome}' foi aprovada, parabéns! Agora aguarde o nosso contato."
    elif instance.status == "rejeitada":
        subject = "Seu cadastro foi rejeitado"
        message = f"Olá {instance.representante},\n\nInfelizmente sua ONG '{instance.nome}' não foi aprovada em nossas análises."
    else:
        return

    send_mail(
        subject,
        message,
        'no-reply@institutocaramelo.com',
        [instance.email],
        fail_silently=False,
    )
