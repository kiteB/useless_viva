# Generated by Django 3.2.5 on 2021-07-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=50)),
                ('result1', models.IntegerField(default=0)),
                ('result2', models.IntegerField(default=0)),
                ('result3', models.IntegerField(default=0)),
                ('result4', models.IntegerField(default=0)),
            ],
        ),
    ]
