# Generated by Django 3.0.8 on 2020-07-25 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encrypt_decrypt_app', '0016_ciphergame_encryptions_used'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciphergame',
            old_name='question',
            new_name='cipher_text',
        ),
        migrations.RenameField(
            model_name='ciphergame',
            old_name='answer',
            new_name='plain_text',
        ),
    ]
