# Generated by Django 3.0.8 on 2020-07-21 12:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date of Birth'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=1, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='photos'),
        ),
    ]
