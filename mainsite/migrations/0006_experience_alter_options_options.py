# Generated by Django 4.0.3 on 2022-04-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=80)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('current', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='options',
            options={'verbose_name_plural': 'Basic Options'},
        ),
    ]
