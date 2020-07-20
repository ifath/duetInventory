# Generated by Django 3.0.8 on 2020-07-15 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Category Name')),
                ('details', models.CharField(max_length=500, verbose_name='Category Details')),
                ('parent_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='product.Category')),
            ],
        ),
    ]
