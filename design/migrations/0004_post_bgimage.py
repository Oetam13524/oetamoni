# Generated by Django 4.0.2 on 2022-03-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bgimage',
            field=models.ImageField(null=True, upload_to='bgimages'),
        ),
    ]
