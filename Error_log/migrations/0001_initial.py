# Generated by Django 4.2.7 on 2023-12-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploaded_files/')),
                ('language', models.CharField(max_length=50)),
                ('error_message', models.TextField()),
                ('threat_level', models.IntegerField()),
                ('upload_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
