# Generated by Django 3.1.6 on 2021-02-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
