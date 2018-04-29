# Generated by Django 2.0.4 on 2018-04-29 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('orgUnit', models.CharField(max_length=10)),
                ('client', models.CharField(max_length=30)),
                ('justification', models.TextField()),
                ('objectives', models.TextField()),
                ('cost_estimates', models.CharField(max_length=60)),
            ],
        ),
    ]
