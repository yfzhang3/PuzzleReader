# Generated by Django 4.0.2 on 2022-02-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_book_image_alter_book_num_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='images/221182406_998264654304104_3219754300096054984_n.png', upload_to='media/'),
        ),
    ]