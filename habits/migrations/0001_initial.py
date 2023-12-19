# Generated by Django 3.1.1 on 2023-12-18 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habit_text', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date started')),
                ('task_completed', models.IntegerField(default=0)),
            ],
        ),
    ]
