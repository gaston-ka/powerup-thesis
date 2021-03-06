# Generated by Django 4.0.4 on 2022-04-30 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, help_text='Address', max_length=250),
        ),
        migrations.AlterField(
            model_name='client',
            name='dob',
            field=models.DateField(blank=True, help_text='Date of Birth', max_length=250),
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('NONE', 'NONE')], help_text='Gender', max_length=250),
        ),
        migrations.AlterField(
            model_name='client',
            name='marital_status',
            field=models.CharField(blank=True, help_text='Marital Status', max_length=250),
        ),
    ]
