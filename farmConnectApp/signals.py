from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserModel

@receiver(post_save, sender=UserModel)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        refresh = RefreshToken.for_user(instance)
        print(f"Access Token: {str(refresh.access_token)}")