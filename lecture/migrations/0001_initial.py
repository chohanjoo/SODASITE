# Generated by Django 2.1.5 on 2019-03-15 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('professor', models.CharField(max_length=50)),
                ('year', models.IntegerField(verbose_name='year')),
                ('semester', models.IntegerField(verbose_name='semester')),
                ('evalue', models.TextField()),
                ('testfile', models.FileField(null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
