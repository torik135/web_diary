# Generated by Django 3.0.3 on 2020-08-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('isi', models.TextField()),
                ('tanggal', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
