# Generated by Django 2.0.2 on 2018-05-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DistributionNodes',
            fields=[
                ('nodeID', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
