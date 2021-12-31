# Generated by Django 3.2.9 on 2021-11-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20211102_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='potasium',
        ),
        migrations.RemoveField(
            model_name='kindinstance',
            name='kind',
        ),
        migrations.AddField(
            model_name='food',
            name='potassium',
            field=models.IntegerField(blank=True, null=True, verbose_name='Amount of potassium'),
        ),
        migrations.AlterField(
            model_name='food',
            name='kind',
            field=models.CharField(blank=True, choices=[('b', 'Bread'), ('f', 'Fruit'), ('m', 'Meat'), ('g', 'Greens'), ('w', 'Water'), ('c', 'Caffeine')], default='m', help_text='Kind of food', max_length=1),
        ),
        migrations.DeleteModel(
            name='Kind',
        ),
    ]
