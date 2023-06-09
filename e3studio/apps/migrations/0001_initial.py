# Generated by Django 2.2.10 on 2020-08-30 03:48

import apps.ultilities
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appname', models.CharField(max_length=200, null=True)),
                ('content', models.TextField(max_length=500, null=True)),
                ('front_image', models.ImageField(blank=True, null=True, upload_to=apps.ultilities.appname_image_path_front, verbose_name='front image')),
                ('top_image', models.ImageField(blank=True, null=True, upload_to=apps.ultilities.appname_image_path_top, verbose_name='top image')),
                ('web', models.TextField(max_length=500, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
