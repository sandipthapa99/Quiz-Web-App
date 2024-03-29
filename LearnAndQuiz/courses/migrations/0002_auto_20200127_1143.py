# Generated by Django 3.0.1 on 2020-01-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.CharField(default=None, max_length=1000)),
                ('image', models.ImageField(default=None, upload_to='courses/images')),
            ],
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
    ]
