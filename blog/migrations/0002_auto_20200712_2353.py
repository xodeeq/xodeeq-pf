# Generated by Django 3.0.8 on 2020-07-12 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='BlogPost',
        ),
    ]
