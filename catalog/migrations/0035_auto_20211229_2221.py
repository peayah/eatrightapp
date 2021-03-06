# Generated by Django 3.2.9 on 2021-12-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0034_alter_food_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='fat',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=4, null=True, verbose_name='Amount of fat'),
        ),
        migrations.AlterField(
            model_name='food',
            name='iron',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=4, null=True, verbose_name='Amount of iron'),
        ),
        migrations.AlterField(
            model_name='food',
            name='magnesium',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=4, null=True, verbose_name='Amount of magnesium'),
        ),
        migrations.AlterField(
            model_name='food',
            name='potassium',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=4, null=True, verbose_name='Amount of potassium'),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=4, null=True, verbose_name='Amount of protein'),
        ),
    ]
