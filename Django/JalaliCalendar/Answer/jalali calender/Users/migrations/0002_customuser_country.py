# Generated by Django 3.2.7 on 2021-12-27 19:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=models.CharField(default='Iran', max_length=4),
        ),
    ]
