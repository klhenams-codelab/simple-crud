# Generated by Django 3.2.12 on 2022-05-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20220502_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosisFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='diagnosis')),
                ('upload_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
