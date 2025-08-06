from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, BuyerProfile, SellerProfile

@receiver(post_save, sender=CustomUser)
def create_user_profiles(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'buyer':
            BuyerProfile.objects.create(user=instance)
        elif instance.role == 'seller':
            SellerProfile.objects.create(user=instance)
        elif instance.role == 'both':
            BuyerProfile.objects.create(user=instance)
            SellerProfile.objects.create(user=instance)
