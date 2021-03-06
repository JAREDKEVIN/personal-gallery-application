# Generated by Django 3.2.7 on 2021-09-04 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20210904_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.category'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.location'),
        ),
    ]
