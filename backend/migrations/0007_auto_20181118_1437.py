# Generated by Django 2.1.1 on 2018-11-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20181105_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='topic_voted',
            field=models.CharField(max_length=200),
        ),
    ]