# Generated by Django 2.2 on 2023-05-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gene', '0011_auto_20230521_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='gene',
            name='middle_type',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
