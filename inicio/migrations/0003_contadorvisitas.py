# Generated by Django 5.2 on 2025-05-23 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_respuestaencuesta'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContadorVisitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitas', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
