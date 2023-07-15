from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import accounts


def accounts_profile(sender, instance, create, **kwargs):
    if create:
        group = Group.objects.get(name='accounts')
        instance.groups.add(group)
        accounts.objects.create(
            user=instance,
            name=instance.username

        )
        print('profile created!')


post_save.connect(accounts_profile, sender=User)
