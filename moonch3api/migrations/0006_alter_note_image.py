# Generated by Django 4.0.4 on 2022-08-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moonch3api', '0005_alter_note_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, default='defaults.png', null=True, upload_to='images/'),
        ),
    ]
