# Generated by Django 3.0.8 on 2020-07-26 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encrypt_decrypt_app', '0017_auto_20200724_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciphergame',
            name='solved',
            field=models.TextField(blank=True, null=True),
        ),
    ]
