# Generated by Django 3.1.6 on 2021-02-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='phone',
            field=models.IntegerField(default=11),
            preserve_default=False,
        ),
    ]
