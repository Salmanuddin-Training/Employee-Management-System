# Generated by Django 3.2 on 2023-08-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Eid', models.BigIntegerField()),
                ('Ename', models.CharField(max_length=255)),
                ('Esal', models.IntegerField()),
                ('Design', models.CharField(max_length=255)),
                ('Company', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254)),
                ('Join_Date', models.DateField()),
                ('City', models.DateField()),
            ],
        ),
    ]
