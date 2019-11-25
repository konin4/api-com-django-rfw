# Generated by Django 2.2.7 on 2019-11-23 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30)),
                ('senha', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=40)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendapp.Login')),
            ],
        ),
    ]