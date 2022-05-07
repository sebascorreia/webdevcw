# Generated by Django 3.0.5 on 2022-05-03 17:43

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0008_doctor_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='location',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='1234567890', max_length=128, null=True, region=None, unique=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
