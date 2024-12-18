# Generated by Django 5.1.2 on 2024-11-01 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nome_categoria', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Doenca',
            fields=[
                ('id_doenca', models.AutoField(primary_key=True, serialize=False)),
                ('nome_doenca', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manejo',
            fields=[
                ('id_manejo', models.AutoField(primary_key=True, serialize=False)),
                ('nome_manejo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id_medicamento', models.AutoField(primary_key=True, serialize=False)),
                ('nome_medicamento', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id_raca', models.AutoField(primary_key=True, serialize=False)),
                ('nome_raca', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id_manutencao', models.AutoField(primary_key=True, serialize=False)),
                ('nome_manutencao', models.CharField(max_length=255)),
                ('id_doenca', models.ForeignKey(blank=True, db_column='id_doenca', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ovinogestApp.doenca')),
                ('id_manejo', models.ForeignKey(blank=True, db_column='id_manejo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ovinogestApp.manejo')),
                ('id_medicamento', models.ForeignKey(blank=True, db_column='id_medicamento', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ovinogestApp.medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='Ovino',
            fields=[
                ('id_ovino', models.AutoField(primary_key=True, serialize=False)),
                ('matricula', models.CharField(max_length=20, unique=True)),
                ('nome_ovino', models.CharField(max_length=255)),
                ('sexo_ovino', models.CharField(max_length=1)),
                ('data_nasc', models.DateField()),
                ('data_cad', models.CharField(max_length=20)),
                ('peso_ovino', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_categoria', models.ForeignKey(blank=True, db_column='id_categoria', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ovinogestApp.categoria')),
                ('id_raca', models.ForeignKey(blank=True, db_column='id_raca', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ovinogestApp.raca')),
            ],
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id_historico', models.AutoField(primary_key=True, serialize=False)),
                ('nome_historico', models.CharField(max_length=255)),
                ('data_historico', models.CharField(max_length=20)),
                ('id_manutencao', models.ForeignKey(blank=True, db_column='id_manutencao', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ovinogestApp.manutencao')),
                ('id_ovino', models.ForeignKey(blank=True, db_column='id_ovino', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ovinogestApp.ovino')),
            ],
        ),
    ]
