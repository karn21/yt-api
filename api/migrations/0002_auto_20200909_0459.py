# Generated by Django 2.2 on 2020-09-09 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-publish_timestamp']},
        ),
    ]
