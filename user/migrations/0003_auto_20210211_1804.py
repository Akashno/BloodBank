# Generated by Django 3.1.6 on 2021-02-11 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_bloodrequest_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='blood_units',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
