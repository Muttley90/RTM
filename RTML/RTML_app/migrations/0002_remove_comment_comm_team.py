# Generated by Django 2.1.7 on 2019-07-16 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RTML_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Comm_team',
        ),
    ]