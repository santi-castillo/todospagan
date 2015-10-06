# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('comentario', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('fecha_compra', models.DateField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('fecha_evento', models.DateField()),
                ('compras', models.ManyToManyField(to='eventos.Compra')),
            ],
        ),
        migrations.CreateModel(
            name='PagoCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('fecha_pago', models.DateTimeField()),
                ('compra', models.ForeignKey(to='eventos.Compra')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='pagocompra',
            name='persona',
            field=models.ForeignKey(to='eventos.Persona'),
        ),
        migrations.AddField(
            model_name='evento',
            name='personas_invitadas',
            field=models.ManyToManyField(to='eventos.Persona'),
        ),
        migrations.AddField(
            model_name='compra',
            name='compradores',
            field=models.ManyToManyField(to='eventos.Persona', related_name='compradores'),
        ),
        migrations.AddField(
            model_name='compra',
            name='responsable',
            field=models.ForeignKey(to='eventos.Persona', related_name='responsable'),
        ),
        migrations.AddField(
            model_name='comentariocompra',
            name='autor',
            field=models.ForeignKey(to='eventos.Persona'),
        ),
    ]
