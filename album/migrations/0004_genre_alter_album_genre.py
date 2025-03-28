# Generated by Django 5.1.6 on 2025-02-12 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_alter_album_options_remove_album_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='album_genre', to='album.genre'),
        ),
    ]
