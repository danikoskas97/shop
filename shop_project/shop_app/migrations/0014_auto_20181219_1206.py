# Generated by Django 2.1.3 on 2018-12-19 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0013_commentresponse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentresponse',
            old_name='product',
            new_name='comment',
        ),
    ]