# Generated by Django 4.2.5 on 2023-10-10 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topics',
            field=models.ManyToManyField(related_name='posts', to='blog.topic'),
        ),
    ]
