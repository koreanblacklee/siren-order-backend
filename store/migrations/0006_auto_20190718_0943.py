# Generated by Django 2.2.2 on 2019-07-18 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20190718_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='city_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='city_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='gungu',
            old_name='gungu_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='gungu',
            old_name='gungu_name',
            new_name='name',
        ),
    ]