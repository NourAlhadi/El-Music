# Generated by Django 2.0 on 2019-01-26 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190126_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='person',
            field=models.CharField(default='', max_length=50),
        ),
    ]