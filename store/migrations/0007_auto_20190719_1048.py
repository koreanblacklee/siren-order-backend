# Generated by Django 2.2.2 on 2019-07-19 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20190718_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gungu',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.City'),
        ),
        migrations.AlterField(
            model_name='store',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.City'),
        ),
        migrations.AlterField(
            model_name='store',
            name='gungu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Gungu'),
        ),
    ]
