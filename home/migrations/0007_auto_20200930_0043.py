# Generated by Django 3.0.5 on 2020-09-29 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200929_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='rent',
            new_name='rent_agreement',
        ),
    ]