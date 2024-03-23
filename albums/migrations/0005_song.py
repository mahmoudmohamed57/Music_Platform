# Generated by Django 4.1.2 on 2022-10-18 16:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_remove_album_creation_datetime_album_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('audio', models.FileField(upload_to='audio/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.album')),
            ],
        ),
    ]
