# Generated by Django 4.0.2 on 2022-03-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0004_post_bgimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.CharField(max_length=200, null=True),
        ),
    ]