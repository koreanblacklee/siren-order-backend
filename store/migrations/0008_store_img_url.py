# Generated by Django 2.2.2 on 2019-07-22 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20190719_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='img_url',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
