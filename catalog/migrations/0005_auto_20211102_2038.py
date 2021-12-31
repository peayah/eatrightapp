# Generated by Django 3.2.9 on 2021-11-03 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20211102_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kindinstance',
            name='kind',
        ),
        migrations.AlterField(
            model_name='food',
            name='kind',
            field=models.CharField(blank=True, choices=[('b', 'Bread'), ('f', 'Fruit'), ('m', 'Meat'), ('g', 'Greens'), ('w', 'Water'), ('c', 'Caffeine')], default='m', help_text='Kind of food', max_length=1),
        ),
        migrations.DeleteModel(
            name='Kind',
        ),
        migrations.DeleteModel(
            name='KindInstance',
        ),
    ]
