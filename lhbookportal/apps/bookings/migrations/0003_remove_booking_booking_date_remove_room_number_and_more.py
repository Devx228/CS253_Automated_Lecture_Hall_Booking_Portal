# Generated by Django 5.1.7 on 2025-03-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_booking_booking_date_booking_cost_booking_duration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_date',
        ),
        migrations.RemoveField(
            model_name='room',
            name='number',
        ),
        migrations.AddField(
            model_name='booking',
            name='need_ac',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='need_projector',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='L-1', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='cost',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
