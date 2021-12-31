from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
import uuid  # Required for unique tool instances


class Food(models.Model):
    """Model representing a food item"""
    name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    calories = models.IntegerField('Amount of calories',
                                   null=True,
                                   blank=True)

    fat = models.DecimalField('Amount of fat',
                              decimal_places=2,
                              max_digits=8,
                                   null=True,
                                   blank=True)

    protein = models.DecimalField('Amount of protein',
                                  decimal_places=2,
                                  max_digits=8,
                                  null=True,
                                    blank=True)

    iron = models.DecimalField('Amount of iron',
                               decimal_places=2,
                               max_digits=8,
                               null=True,
                                   blank=True)

    potassium = models.DecimalField('Amount of potassium',
                                    decimal_places=2,
                                    max_digits=8,
                                    null=True,
                                    blank=True)

    magnesium = models.DecimalField('Amount of magnesium',
                                    decimal_places=2,
                                    max_digits=8,
                                    null=True,
                                    blank=True)

    KIND_OF_FOOD = (
        ('b', 'Bread'),
        ('f', 'Fruit'),
        ('m', 'Meat'),
        ('g', 'Greens'),
        ('w', 'Water'),
        ('c', 'Caffeine'),
        ('o', 'Oil'),
        ('x', 'Extra')
    )

    kind = models.CharField(
        max_length=1,
        choices=KIND_OF_FOOD,
        blank=True,
        default='m',
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


class FoodInstance(models.Model):

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          help_text='Unique ID across whole collection')

    food = models.ForeignKey('Food',
                             default=None,
                             on_delete=models.RESTRICT,
                             null=True)

    eater = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              null=True,
                              default=User)


    consumed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return '{self.id} ({self.food.name})'

    def get_absolute_url(self):
        return reverse('index')


class DailyIntake(models.Model):
    max_bread = models.IntegerField('Total of bread', null=True, blank=True)
    max_fruit = models.IntegerField('Total of fruit', null=True, blank=True)
    max_meat = models.IntegerField('Total of meat', null=True, blank=True)
    max_greens = models.IntegerField('Total of greens', null=True, blank=True)
    max_water = models.IntegerField('Total of water', null=True, blank=True)
    max_caffeine = models.IntegerField('Total of caffeine', null=True, blank=True)
    max_calories = models.IntegerField('Total of calories', null=True, blank=True)
    max_fat = models.IntegerField('Total of fat', null=True, blank=True)
    max_protein = models.IntegerField('Total of protein', null=True, blank=True)
    max_iron = models.IntegerField('Total of iron', null=True, blank=True)
    max_potassium = models.IntegerField('Total of potassium', null=True, blank=True)
    max_magnesium = models.IntegerField('Total of magnesium', null=True, blank=True)
    max_oil = models.IntegerField('Total of oil',      null=True, blank=True)

