# Generated by Django 2.2.2 on 2019-09-06 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inbox',
            name='starred',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Starred',
        ),
    ]
