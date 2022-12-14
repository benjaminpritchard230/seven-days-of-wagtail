# Generated by Django 4.1.2 on 2022-10-30 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('generic', '0002_genericpage_introduction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='banner_image',
            field=models.ForeignKey(blank='False', null='True', on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
            preserve_default='True',
        ),
    ]
