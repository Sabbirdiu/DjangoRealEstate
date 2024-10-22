# Generated by Django 3.0.5 on 2020-09-29 08:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_listing_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rent',
            field=models.CharField(choices=[('M', 'M'), ('Y', 'Y')], max_length=30, null=True),
        ),
    ]
