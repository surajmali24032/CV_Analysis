# Generated by Django 4.0.4 on 2022-05-04 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='Question',
            new_name='question',
        ),
    ]
