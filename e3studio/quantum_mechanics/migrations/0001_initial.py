# Generated by Django 2.2.10 on 2020-09-23 07:17

from django.db import migrations, models
import django.db.models.deletion
import quantum_mechanics.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, max_length=2, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=100, null=True)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=quantum_mechanics.models.chapter_cover_path, verbose_name='chapter image')),
                ('top', models.ImageField(blank=True, null=True, upload_to=quantum_mechanics.models.chapter_cover_path, verbose_name='chapter top')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=200, null=True)),
                ('chapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quantum_mechanics.Chapter')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField(max_length=5000, null=True)),
                ('chapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quantum_mechanics.Chapter')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quantum_mechanics.Section')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_image', models.ImageField(blank=True, null=True, upload_to=quantum_mechanics.models.section_image_path, verbose_name='section image')),
                ('caption', models.TextField(blank=True, max_length=5000, null=True)),
                ('chapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quantum_mechanics.Chapter')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quantum_mechanics.Section')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.TextField(max_length=5000, null=True)),
                ('chapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quantum_mechanics.Chapter')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quantum_mechanics.Section')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_1', models.TextField(max_length=500, null=True)),
                ('choice_2', models.TextField(max_length=500, null=True)),
                ('choice_3', models.TextField(max_length=500, null=True)),
                ('answer', models.CharField(choices=[('A', models.TextField(max_length=500, null=True)), ('B', models.TextField(max_length=500, null=True)), ('C', models.TextField(max_length=500, null=True))], default='A', max_length=1, null=True)),
                ('comment_1', models.TextField(blank=True, max_length=500, null=True)),
                ('equation_1', models.TextField(blank=True, max_length=500, null=True)),
                ('comment_2', models.TextField(blank=True, max_length=500, null=True)),
                ('equation_2', models.TextField(blank=True, max_length=500, null=True)),
                ('chapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quantum_mechanics.Chapter')),
                ('exercise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quantum_mechanics.Exercise')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quantum_mechanics.Section')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
