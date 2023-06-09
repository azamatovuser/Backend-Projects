from django.contrib import admin
from apps.account.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','image_tag', 'bio')