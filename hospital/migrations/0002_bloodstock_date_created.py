# Generated by Django 3.1.6 on 2021-02-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodstock',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
