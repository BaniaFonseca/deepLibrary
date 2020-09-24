# Generated by Django 3.1.1 on 2020-09-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200924_0448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='5f6c6e548fca3222f60098b1', max_length=24, primary_key=True, serialize=False),
        ),
    ]