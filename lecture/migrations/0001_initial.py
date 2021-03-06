# Generated by Django 2.1.7 on 2019-10-18 07:29

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
                ('name', models.CharField(max_length=50, verbose_name='강의명')),
                ('professor', models.CharField(max_length=50, verbose_name='교수님')),
                ('year', models.IntegerField(verbose_name='수강년도')),
                ('semester', models.IntegerField(verbose_name='수강학기')),
                ('evalue', models.TextField(verbose_name='강의평')),
                ('examfile', models.FileField(blank=True, upload_to='lecture', verbose_name='족보파일')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
