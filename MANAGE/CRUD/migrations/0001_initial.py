# Generated by Django 5.0.2 on 2024-03-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('m_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('mname', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
