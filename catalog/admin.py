# source env/bin/activate
# virtual server: python3 manage.py runserver

from django.contrib import admin
from .models import Food, FoodInstance, DailyIntake
# from.models import User
# from django.contrib import UserAdmin as BaseUserAdmin

from import_export.admin import ImportExportMixin

@admin.register(DailyIntake)
class DailyIntakeAdmin(admin.ModelAdmin):
    list_display = ('max_bread',
                    'max_fruit',
                    'max_meat',
                    'max_greens',
                    'max_water',
                    'max_caffeine',
                    'max_calories',
                    'max_fat',
                    'max_protein',
                    'max_iron',
                    'max_potassium',
                    'max_magnesium',
                    'max_oil',
                    )
    fieldsets = (
        ('Solids', {'fields': ('max_bread', 'max_fruit', 'max_meat','max_greens', 'max_oil')
                }),

        ('Liquids', {'fields': ('max_water', 'max_caffeine')
                    }),

        ('Nutrients', {'fields': ('max_calories', 'max_fat', 'max_protein',
                                  'max_iron', 'max_potassium', 'max_magnesium')
        }),
    )


@admin.register(Food)
class FoodAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'kind', 'calories', 'fat', 'protein', 'iron', 'potassium', 'magnesium')
    fieldsets = (
        (None, {'fields': ('name', 'kind')
                }),
        ('Details', {
            'fields': ( 'calories', 'fat', 'protein', 'iron', 'potassium', 'magnesium')
        }),
    )


@admin.register(FoodInstance)
class FoodInstanceAdmin(admin.ModelAdmin):
    list_display = ('food', 'eater', 'id', 'consumed')
