# Generated by Django 3.0 on 2019-12-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_remove_listing_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price_per_month',
            field=models.IntegerField(default=10, help_text='Enter rent price per month'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='total_area',
            field=models.DecimalField(decimal_places=2, default=10, help_text='Enter the total square feet of your space', max_digits=7),
            preserve_default=False,
        ),
    ]
