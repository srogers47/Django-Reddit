# Generated by Django 3.1.5 on 2021-02-13 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0003_post_comment_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
    ]
