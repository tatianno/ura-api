# Generated by Django 5.1.3 on 2024-12-03 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('documento', models.CharField(max_length=50)),
                ('em_massiva', models.BooleanField(default=False)),
            ],
        ),
    ]
