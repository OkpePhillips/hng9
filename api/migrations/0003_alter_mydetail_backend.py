# Generated by Django 4.1.2 on 2022-10-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_bio_mydetail_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydetail',
            name='backend',
            field=models.BooleanField(default=True),
        ),
    ]