# Generated by Django 4.0.4 on 2022-08-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moonch3api', '0002_message_images_note_images_alter_user_table_mindset_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, default='defaults.png', null=True, upload_to='images/'),
        ),
    ]