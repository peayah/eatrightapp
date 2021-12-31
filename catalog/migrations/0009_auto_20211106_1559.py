# Generated by Django 3.2.9 on 2021-11-06 22:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_foodinstance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodinstance',
            name='status',
        ),
        migrations.AddField(
            model_name='food',
            name='status',
            field=models.CharField(blank=True, choices=[('x', 'Eaten'), ('o', 'Not Eaten')], default='m', help_text='Was it eaten', max_length=1),
        ),
        migrations.AlterField(
            model_name='food',
            name='kind',
            field=models.CharField(blank=True, choices=[('b', 'Bread'), ('f', 'Fruit'), ('m', 'Meat'), ('g', 'Greens'), ('w', 'Water'), ('c', 'Caffeine'), ('o', 'Oil')], default='m', help_text='Kind of food', max_length=1),
        ),
        migrations.AlterField(
            model_name='foodinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this food instance across whole collection', primary_key=True, serialize=False),
        ),
    ]