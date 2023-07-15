from django.contrib import admin
from accounts.models import accounts
# Register your models here.


class accountsAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password1', 'password2')


admin.site.register(accounts, accountsAdmin,)
