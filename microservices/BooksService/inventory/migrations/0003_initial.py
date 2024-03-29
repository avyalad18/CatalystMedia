# Generated by Django 5.0.3 on 2024-03-17 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0002_delete_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('authors', models.CharField(max_length=20)),
                ('isbn', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
            options={
                'db_table': 'Books',
                'managed': True,
            },
        ),
    ]
