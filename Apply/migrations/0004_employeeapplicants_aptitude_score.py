# Generated by Django 3.1.1 on 2020-12-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0003_aptitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeapplicants',
            name='aptitude_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
