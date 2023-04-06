from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/')
    bio = models.CharField(max_length=221, null=True, blank=True)

    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        return self.user.username

    @property
    def get_full_name(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.last_name} {self.user.first_name}"
        return f"{self.user.username}"


def post_save_profile(instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user_id=instance.id)


post_save.connect(post_save_profile, sender=User)