# Generated by Django 4.1.2 on 2022-10-11 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True, verbose_name='Название Автомобиля')),
                ('image', models.ImageField(null=True, upload_to=' ')),
            ],
        ),
    ]