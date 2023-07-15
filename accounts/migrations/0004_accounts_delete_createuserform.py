# Generated by Django 4.2.3 on 2023-07-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_createuserform_delete_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('password1', models.CharField(max_length=200, null=True)),
                ('password2', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CreateUserform',
        ),
    ]