from django.urls import path
from . import views
from django.conf.urls import url
from django_filters.views import FilterView
from django_filters.views import object_filter
from .models import Food, DailyIntake


urlpatterns = [
    path('',
         views.index,
         name='index'),

    path('consumedfood/',
         views.ConsumedFoodListView.as_view(),
         name = 'all-consumed'),

    path('filtered_list/',
         views.food_list,
         name = 'filtered-list'),

    path('food/',
         views.FoodListView.as_view(),
         name = 'all-food'),

    path('notes/',
         views.NotesPageView.as_view(),
         name = 'notes'),

    path('food/create/',
         views.FoodCreate.as_view(),
         name = 'food-create'),

    path('foodinstance/create/',
         views.FoodInstanceCreate.as_view(),
         name = 'foodinstance-create'),

    path('foodinstance/<pk>/delete/',
         views.FoodInstanceDelete.as_view(),
         name='foodinstance-delete'),

    path('dailyintake/',
         views.DailyIntakeView.as_view(),
         name="user-settings"),

    path('dailyintake/<slug:pk>/',
         views.DailyIntakeUpdate.as_view(),
         name='settings_update'),



    url(r'^list$', views.food_list),
    # url(r'^list/$', FilterView.as_view(model=Food)),
    # url(r'^list/$', object_filter, {'model': Food}),
]
