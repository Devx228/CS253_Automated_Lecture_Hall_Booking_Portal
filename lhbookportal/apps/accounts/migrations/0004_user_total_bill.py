# Generated by Django 5.1.7 on 2025-03-22 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_authority_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='total_bill',
            field=models.IntegerField(default=0),
        ),
    ]
