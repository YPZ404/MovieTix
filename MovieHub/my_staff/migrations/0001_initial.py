# Generated by Django 3.2 on 2022-10-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('release_id', models.IntegerField()),
                ('room_id', models.IntegerField()),
                ('row_id', models.IntegerField()),
                ('column_id', models.IntegerField()),
                ('is_available', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Seat',
            },
        ),
    ]
