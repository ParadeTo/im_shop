from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

# apps 中设置
"""
    def ready(self):
        import users.signals
"""
@receiver(post_save, sender=User)
def create_user_token(sender, instance=None, created=False, **kwargs):
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()

