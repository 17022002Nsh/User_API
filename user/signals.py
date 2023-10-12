from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from user.models import User, Token



@receiver(post_save, sender=User)
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
    if not created:
        pass    
    