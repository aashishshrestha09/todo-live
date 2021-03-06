# Generated by Django 3.0.6 on 2020-05-07 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_todo',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='add_todo',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='add_todo',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
