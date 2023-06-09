# Generated by Django 2.2.10 on 2020-06-24 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20200512_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='province',
            field=models.CharField(blank=True, choices=[('Alberta', 'Alberta'), ('British Columbia', 'British Columbia'), ('Manitoba', 'Manitoba'), ('New Brunswick', 'New Brunswick'), ('Newfoundland and Labrador', 'Newfoundland and Labrador'), ('Northwest Territories', 'Northwest Territories'), ('Nova Scotia', 'Nova Scotia'), ('Nunavut', 'Nunavut'), ('Ontario', 'Ontario'), ('Prince Edward Island', 'Prince Edward Island'), ('Quebec', 'Quebec'), ('Saskatchewan', 'Saskatchewan'), ('Yukon', 'Yukon')], default='British Columbia', max_length=30),
        ),
    ]
