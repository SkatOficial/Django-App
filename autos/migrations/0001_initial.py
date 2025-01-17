# Generated by Django 4.1.2 on 2024-07-13 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id_auto', models.AutoField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=30)),
                ('año', models.IntegerField()),
                ('transmision', models.CharField(max_length=30)),
                ('motor', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='img/')),
                ('velocidades', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.marca')),
            ],
        ),
    ]
