import django_filters
from .models import Food


class FoodFilter(django_filters.FilterSet):
    kind = django_filters.CharFilter(lookup_expr='iexact')
    calories = django_filters.RangeFilter()
    fat = django_filters.RangeFilter()
    protein = django_filters.RangeFilter()
    iron = django_filters.RangeFilter()
    magnesium = django_filters.RangeFilter()
    potassium = django_filters.RangeFilter()

    class Meta:
        model = Food
        fields = ['kind', 'calories', 'fat', 'protein', 'iron', 'magnesium', 'potassium']
