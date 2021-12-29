# Generated by Django 3.2.10 on 2021-12-29 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_gigpackage_package_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gigpackage',
            name='package_type',
            field=models.IntegerField(blank=True, choices=[(1, 'Basic'), (2, 'Standard'), (3, 'Premium')], null=True),
        ),
    ]