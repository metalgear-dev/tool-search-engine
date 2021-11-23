# Generated by Django 3.2.7 on 2021-11-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0004_auto_20211119_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonePermanent',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('tooling', models.CharField(db_column='Tooling', max_length=255, verbose_name='Tooling')),
                ('tnum', models.IntegerField(db_column='TNumber', default=0, verbose_name='TNumber')),
            ],
            options={
                'db_table': 'Non_Permanent',
            },
        ),
    ]
