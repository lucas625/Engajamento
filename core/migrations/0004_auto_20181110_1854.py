# Generated by Django 2.1.3 on 2018-11-10 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
