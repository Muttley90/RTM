# Generated by Django 2.1.7 on 2019-07-16 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RTML_app', '0003_comment_comm_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Comm_team',
        ),
        migrations.RemoveField(
            model_name='team',
            name='Team_serv',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]