# Generated by Django 2.2.6 on 2021-01-26 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_user', to=settings.AUTH_USER_MODEL, verbose_name='follow_user')),
                ('followed_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_user', to=settings.AUTH_USER_MODEL, verbose_name='followed_user')),
            ],
        ),
    ]
