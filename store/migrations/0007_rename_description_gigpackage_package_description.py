# Generated by Django 3.2.10 on 2021-12-29 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_gig_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gigpackage',
            old_name='description',
            new_name='package_description',
        ),
    ]
