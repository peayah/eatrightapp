# Generated by Django 3.2.8 on 2021-11-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Food Item', max_length=200)),
                ('calories', models.IntegerField(blank=True, null=True, verbose_name='Amount of calories')),
                ('potasium', models.IntegerField(blank=True, null=True, verbose_name='Amount of potasium')),
                ('kind', models.CharField(blank=True, choices=[('b', 'Bread'), ('f', 'Fruit'), ('m', 'Meat'), ('g', 'Greens'), ('w', 'Water'), ('c', 'Caffine')], default='m', help_text='Kind of food', max_length=1)),
            ],
        ),
    ]
