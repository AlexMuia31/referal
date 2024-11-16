# Generated by Django 4.2.9 on 2024-02-03 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NomaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('wallet', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'NomaUser',
                'verbose_name_plural': 'NomaUsers',
                'ordering': ['name'],
            },
        ),
    ]