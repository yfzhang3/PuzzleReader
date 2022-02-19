# Generated by Django 4.0.2 on 2022-02-19 17:22

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
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='user', max_length=25)),
                ('title', models.CharField(default='None', max_length=30)),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Fiction', 'Fiction')], default='None', max_length=200)),
                ('bio', models.CharField(max_length=500)),
                ('num_stars', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
