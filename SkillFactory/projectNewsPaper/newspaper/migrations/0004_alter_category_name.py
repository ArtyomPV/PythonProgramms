# Generated by Django 4.2.4 on 2023-09-05 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0003_category_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='History', max_length=255, unique=True),
        ),
    ]
