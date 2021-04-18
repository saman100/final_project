# Generated by Django 3.2 on 2021-04-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('std_number', models.IntegerField()),
                ('teacher', models.CharField(choices=[('ahmadi', 'Ahmadi'), ('adbi', 'Abdi'), ('bahrami', 'Bahrami')], max_length=7)),
            ],
        ),
    ]
