# Generated by Django 3.0.5 on 2020-10-01 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='next_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='news.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='previous_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous', to='news.Post'),
        ),
    ]
