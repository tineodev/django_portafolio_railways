# Generated by Django 4.1.4 on 2022-12-08 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_model_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPs_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50)),
            ],
        ),
    ]
