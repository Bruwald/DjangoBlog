# Generated by Django 2.2.1 on 2019-06-05 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190604_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Blog Date'),
        ),
    ]
