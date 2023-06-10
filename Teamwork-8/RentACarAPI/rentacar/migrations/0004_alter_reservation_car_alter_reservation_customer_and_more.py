# Generated by Django 4.2 on 2023-06-09 19:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rentacar', '0003_reservation_car_reservation_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rentacar.car'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rentacar.customer'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]