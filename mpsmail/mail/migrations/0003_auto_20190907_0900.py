# Generated by Django 2.2.2 on 2019-09-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_auto_20190906_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='inbox',
            name='attach',
            field=models.FileField(default='', upload_to='attach_data/'),
        ),
        migrations.AddField(
            model_name='sentmail',
            name='attach',
            field=models.FileField(default='', upload_to='attach_data/'),
        ),
    ]