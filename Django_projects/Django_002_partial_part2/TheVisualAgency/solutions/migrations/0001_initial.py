# Generated by Django 3.2.8 on 2021-11-09 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=3000)),
                ('video', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CaseStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('path', models.FileField(upload_to='')),
                ('projectObjetive', models.CharField(max_length=2000)),
                ('clientBenefit', models.CharField(max_length=2000)),
                ('projectResult', models.CharField(max_length=2000)),
                ('projectBackground', models.CharField(max_length=3000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solutions.category')),
            ],
            options={
                'db_table': 'caseStudies',
            },
        ),
    ]
