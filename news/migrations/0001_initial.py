# Generated by Django 3.0.5 on 2020-09-28 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('overview', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('featured', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Author')),
            ],
        ),
    ]
