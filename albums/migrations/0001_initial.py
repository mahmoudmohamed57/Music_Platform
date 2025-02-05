# Generated by Django 4.1.2 on 2022-10-08 05:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Album', max_length=255)),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('release_datetime', models.DateTimeField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.artist')),
            ],
        ),
    ]
