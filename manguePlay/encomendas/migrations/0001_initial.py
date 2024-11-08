# Generated by Django 5.1.2 on 2024-11-01 00:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brinquedos', '0003_remove_brinquedo_imagem_alter_brinquedo_preco_imagem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Encomenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('data_encomenda', models.DateTimeField(auto_now_add=True)),
                ('brinquedo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brinquedos.brinquedo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]