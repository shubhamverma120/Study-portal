# Generated by Django 5.0.4 on 2024-04-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_addcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentreg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30)),
                ('sgen', models.CharField(max_length=10)),
                ('sco', models.BigIntegerField(max_length=13)),
                ('email', models.CharField(max_length=30)),
                ('sadd', models.CharField(max_length=40)),
                ('date', models.CharField(default='', max_length=30)),
                ('cpass', models.CharField(default='', max_length=30)),
                ('simg', models.FileField(upload_to='upload')),
            ],
            options={
                'db_table': 'studentreg',
            },
        ),
    ]
