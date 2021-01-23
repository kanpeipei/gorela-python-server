# Generated by Django 2.2.6 on 2021-01-22 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210122_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='posts.Post', verbose_name='post_id'),
        ),
    ]
