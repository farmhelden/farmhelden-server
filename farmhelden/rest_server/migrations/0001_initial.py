# Generated by Django 3.0.4 on 2020-03-20 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zip_code', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
            ],
        ),
    ]