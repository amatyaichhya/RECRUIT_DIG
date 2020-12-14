# Generated by Django 3.1.1 on 2020-12-09 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0002_similarity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aptitude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.IntegerField()),
                ('question', models.CharField(max_length=500)),
                ('opta', models.CharField(max_length=500)),
                ('optb', models.CharField(max_length=500)),
                ('optc', models.CharField(max_length=500)),
                ('optd', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
            ],
        ),
    ]
