# Generated by Django 5.0 on 2024-01-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_member_rollno'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='phoneno',
            field=models.IntegerField(null=True),
        ),
    ]
