# Generated by Django 4.2.5 on 2023-09-16 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='customers',
            name='email',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
