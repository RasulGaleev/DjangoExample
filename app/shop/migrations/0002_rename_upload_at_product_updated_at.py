# Generated by Django 4.2.4 on 2024-03-27 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='upload_at',
            new_name='updated_at',
        ),
    ]
