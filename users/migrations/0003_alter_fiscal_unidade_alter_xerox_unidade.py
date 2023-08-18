# Generated by Django 4.2.3 on 2023-08-16 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unidades', '0001_initial'),
        ('users', '0002_xerox_requisitante_fiscal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiscal',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.unidade'),
        ),
        migrations.AlterField(
            model_name='xerox',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.unidade'),
        ),
    ]
