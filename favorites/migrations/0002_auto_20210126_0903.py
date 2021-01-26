# Generated by Django 2.2.6 on 2021-01-26 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='posts.Post', verbose_name='post'),
        ),
    ]
