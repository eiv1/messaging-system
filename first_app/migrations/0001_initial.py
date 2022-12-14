# Generated by Django 4.0.6 on 2022-11-09 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=256)),
                ('receiver', models.CharField(max_length=256)),
                ('message', models.CharField(max_length=1248)),
                ('subject', models.CharField(max_length=312)),
                ('creation_date', models.DateField()),
                ('read', models.BooleanField(default=False)),
            ],
        ),
    ]
