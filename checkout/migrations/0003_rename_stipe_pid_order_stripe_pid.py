# Generated by Django 3.2 on 2022-02-12 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20220212_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='stipe_pid',
            new_name='stripe_pid',
        ),
    ]
