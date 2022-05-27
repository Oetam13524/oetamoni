# Generated by Django 4.0.2 on 2022-03-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0005_post_excerpt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
