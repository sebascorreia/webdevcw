# Generated by Django 3.0.5 on 2022-05-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(null=True, upload_to='hospital/static/hospital/profile_pics'),
        ),
    ]