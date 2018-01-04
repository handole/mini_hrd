# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 19:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Akun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_akun', models.CharField(choices=[('karyawan', 'Karyawan'), ('admin', 'Admin')], max_length=20)),
                ('akun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Divisi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('keterangan', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('keterangan', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Karyawan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.TextField(blank=True)),
                ('jenis_kelamin', models.CharField(choices=[('pria', 'Pria'), ('wanita', 'Wanita')], max_length=10)),
                ('jenis_karyawan', models.CharField(choices=[('magang', 'Magang'), ('kontrak', 'Kontrak'), ('tetap', 'Tetap')], max_length=10)),
                ('no_telepon', models.CharField(blank=True, max_length=10)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('no_rekening', models.CharField(max_length=100)),
                ('pemilik_rekening', models.CharField(max_length=100)),
                ('divisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karyawan.Divisi')),
                ('jabatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karyawan.Jabatan')),
            ],
        ),
        migrations.AddField(
            model_name='akun',
            name='karyawan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karyawan.Karyawan'),
        ),
    ]
