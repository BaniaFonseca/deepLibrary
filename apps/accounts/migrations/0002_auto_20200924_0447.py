# Generated by Django 3.1.1 on 2020-09-24 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default="<class 'bson.objectid.ObjectId'>", max_length=25, primary_key=True, serialize=False),
        ),
    ]
