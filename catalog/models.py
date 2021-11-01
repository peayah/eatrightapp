from django.db import models
from django.urls import reverse


class Food(models.Model):
    """Model representing a food item"""
    name = models.CharField(max_length=200,
                            help_text='Enter Food Item')

    calories = models.IntegerField('Amount of calories', null=True, blank=True)

    potasium = models.IntegerField('Amount of potasium', null=True, blank=True)

    KIND_OF_FOOD = (
        ('b', 'Bread'),
        ('f', 'Fruit'),
        ('m', 'Meat'),
        ('g', 'Greens'),
        ('w', 'Water'),
        ('c', 'Caffine'),
    )

    kind = models.CharField(
        max_length=1,
        choices=KIND_OF_FOOD,
        blank=True,
        default='m',
        help_text='Kind of food',
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food-detail', args=[str(self.id)])
