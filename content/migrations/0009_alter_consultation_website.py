# Generated by Django 4.0.4 on 2022-05-23 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
