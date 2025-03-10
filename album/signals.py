from django.db.models.signals import pre_save
from django.dispatch import receiver
from album.models import Band


@receiver(pre_save, sender=Band)
def album_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'bio gerada com sucesso'
