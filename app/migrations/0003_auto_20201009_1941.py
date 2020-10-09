# Generated by Django 3.1.2 on 2020-10-09 16:41

import app.models
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_auto_20201009_1855"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="photo",
            field=django_resized.forms.ResizedImageField(
                blank=True,
                crop=None,
                force_format=None,
                keep_meta=True,
                quality=0,
                size=[500, 300],
                upload_to=app.models.get_file_path,
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="photo",
            field=models.ImageField(blank=True, upload_to=app.models.get_file_path),
        ),
    ]