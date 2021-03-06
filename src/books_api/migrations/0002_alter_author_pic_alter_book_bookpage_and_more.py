# Generated by Django 4.0.3 on 2022-04-20 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='pic',
            field=models.FileField(upload_to='author/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookpage',
            field=models.FileField(upload_to='bookpage/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='coverpage',
            field=models.FileField(upload_to='coverpage/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.FileField(upload_to='category/%Y/%m/%d/'),
        ),
    ]
