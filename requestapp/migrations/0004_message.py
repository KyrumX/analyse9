# Generated by Django 2.0.2 on 2018-03-14 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestapp', '0003_auto_20180307_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=5000)),
            ],
        ),
    ]
