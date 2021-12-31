# from django.shortcuts import render
from .models import Food, FoodInstance, DailyIntake
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views import generic
from django.db.models import Sum, Min

# Date and time
import time
from datetime import datetime, timedelta, time
from datetime import *

# Form
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from catalog.models import FoodInstance
from import_export import resources
# from resources import FoodResource
from django.shortcuts import redirect

from catalog.forms import ConsumeFoodForm, \
    ConsumeWaterForm, \
    ConsumeBreadForm, \
    ConsumeMeatForm,\
    ConsumeGreensForm,\
    ConsumeFruitForm,\
    ConsumeCaffeineForm,\
    ConsumeOilForm

# from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.context_processors import request

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.urls import reverse

from django.shortcuts import render
# model and form imports

from .models import Food
from django.shortcuts import render
from .filters import FoodFilter

from tablib import Dataset


def food_list(request):
    f = FoodFilter(request.GET, queryset=Food.objects.all())
    return render(request, 'catalog/filtered_list.html', {'filter': f})

class LoginUserView(LoginView):
    consume_food_form = ConsumeFoodForm
    extra_context = {"consume_water_form": ConsumeWaterForm}
    template_name = 'index.html'


def index(request):

    """ homepage view """

    # if request.user.is_anonymous():
    #     print("user is anonymous")
    # else:
    #     print("user is logged in")

    # Today's meals
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())

    todays_meals = FoodInstance.objects.filter(consumed__lte=today_end,
                                               consumed__gte=today_start)

    # Sums and counts of foods and nutrients for today
    # sum_of_potassium = Food.objects.all().aggregate(Sum('potassium')).get('potassium__sum', 0.00)
    # sum_of_calories = Food.objects.all().aggregate(Sum('calories')).get('calories__sum', 0.00)

    sum_of_calories = FoodInstance.objects.filter(consumed__lte=today_end,
                                                  consumed__gte=today_start).aggregate(
        Sum('food__calories')).get('food__calories__sum', 0.00)

    sum_of_fat = FoodInstance.objects.filter(consumed__lte=today_end,
        consumed__gte=today_start).aggregate(Sum('food__fat')).get('food__fat__sum', 0.00)

    sum_of_protein = FoodInstance.objects.filter(consumed__lte=today_end,
        consumed__gte=today_start).aggregate(Sum('food__protein')).get('food__protein__sum', 0.00)

    sum_of_iron =    FoodInstance.objects.filter(consumed__lte=today_end,
        consumed__gte=today_start).aggregate(Sum('food__iron'   )).get('food__iron__sum', 0.00)

    sum_of_magnesium = FoodInstance.objects.filter(consumed__lte=today_end,
        consumed__gte=today_start).aggregate(Sum('food__magnesium')).get('food__magnesium__sum', 0.00)

    sum_of_potassium = FoodInstance.objects.filter(consumed__lte=today_end,
        consumed__gte=today_start).aggregate(Sum('food__potassium')).get('food__potassium__sum', 0.00)

    num_bread = FoodInstance.objects.filter(food__kind__exact='b').filter(consumed__lte=today_end,
                                                                          consumed__gte=today_start).count()
    num_fruit = FoodInstance.objects.filter(food__kind__exact='f').filter(consumed__lte=today_end,
                                                                          consumed__gte=today_start).count()
    num_meat = FoodInstance.objects.filter(food__kind__exact='m').filter(consumed__lte=today_end,
                                                                         consumed__gte=today_start).count()
    num_greens = FoodInstance.objects.filter(food__kind__exact='g').filter(consumed__lte=today_end,
                                                                           consumed__gte=today_start).count()
    num_water = FoodInstance.objects.filter(food__kind__exact='w').filter(consumed__lte=today_end,
                                                                          consumed__gte=today_start).count()
    num_coffee = FoodInstance.objects.filter(food__kind__exact='c').filter(consumed__lte=today_end,
                                                                           consumed__gte=today_start).count()
    num_oil = FoodInstance.objects.filter(food__kind__exact='o').filter(consumed__lte=today_end,
                                                                        consumed__gte=today_start).count()

    # Maximum intake intances
    intake_instances = DailyIntake.objects.all()

    # Forms
    form = ConsumeFoodForm(request.POST or None)
    bread_form = ConsumeBreadForm(request.POST or None)
    fruit_form = ConsumeFruitForm(request.POST or None)
    meat_form = ConsumeMeatForm(request.POST or None)
    greens_form = ConsumeGreensForm(request.POST or None)
    water_form = ConsumeWaterForm(request.POST or None)
    caffe_form = ConsumeCaffeineForm(request.POST or None)
    oil_form = ConsumeOilForm(request.POST or None)

    if request.method == 'POST':

        if 'consume_food' in request.POST:
            if form.is_valid():
                xf = form.save(commit=True)
                xf.save()
                return redirect('index')

        elif 'consume_bread' in request.POST:
            if bread_form.is_valid():
                bf=bread_form.save(commit=False)
                bf.save()
                return redirect('index')

        elif 'consume_fruit' in request.POST:
            if fruit_form.is_valid():
                ff=fruit_form.save(commit=False)
                ff.save()
                return redirect('index')

        elif 'consume_meat' in request.POST:
            if meat_form.is_valid():
                mf=meat_form.save(commit=False)
                mf.save()
                return redirect('index')

        elif 'consume_greens' in request.POST:
            if greens_form.is_valid():
                gf=greens_form.save(commit=False)
                gf.save()
                return redirect('index')

        elif 'consume_water' in request.POST:
            if water_form.is_valid():
                wf=water_form.save(commit=False)
                wf.save()
                return redirect('index')

        elif 'consume_caffeine' in request.POST:
            if caffe_form.is_valid():
                cf = caffe_form.save(commit=False)
                cf.save()
                return redirect('index')

        elif 'consume_oil' in request.POST:
            if oil_form.is_valid():
                of = oil_form.save(commit=False)
                of.save()
                return redirect('index')


    context = {

        'num_bread': num_bread,
        'num_fruit': num_fruit,
        'num_meat': num_meat,
        'num_greens': num_greens,
        'num_water': num_water,
        'num_coffee': num_coffee,
        'num_oil': num_oil,

        'sum_of_calories': sum_of_calories,
        'sum_of_fat': sum_of_fat,
        'sum_of_protein': sum_of_protein,
        'sum_of_iron': sum_of_iron,
        'sum_of_potassium': sum_of_potassium,
        'sum_of_magnesium': sum_of_magnesium,

        'intake_instances': intake_instances,
        'todays_meals': todays_meals,

        'form': form,
        'water_form': water_form,
        'bread_form':bread_form,
        'fruit_form':fruit_form,
        'meat_form':meat_form ,
        'greens_form':greens_form,
        'caffe_form':caffe_form,
        'oil_form':oil_form,
        }

    return render(request, 'index.html', context=context)


class ConsumedFoodListView(LoginRequiredMixin, generic.ListView):
    # (LoginRequiredMixin,generic.ListView):
    model = FoodInstance
    template_name = 'catalog/foodinstance_list_consumed.html'
    paginate_by = 50

    def get_queryset(self):

        this_day = datetime.today()

        # filter on time stamp only showing food listed
        # from same month
        return FoodInstance.objects.filter(consumed__month=this_day.month)


class FoodListView(LoginRequiredMixin, generic.ListView):
    # (LoginRequiredMixin,generic.ListView):
    model = Food
    paginate_by = 50
    template_name = 'catalog/foodlist.html'

    def get_queryset(self):
        return Food.objects.all()


class FoodCreate(CreateView):
    model = Food
    fields = ['name', 'calories', 'fat',  'protein', 'iron', 'potassium', 'magnesium', 'kind']


class FoodInstanceCreate(CreateView):
    model = FoodInstance
    consumed = True
    eater = "me"
    fields = ['food', 'eater']

    success_url = reverse_lazy("foodinstance-create")

    def get_initial(self):
        return {'eater': self.request.user}



    def get_context_data(self, **kwargs):
        # Today's meals
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())

        context = super(FoodInstanceCreate, self).get_context_data(**kwargs)
        # user = self.request.user
        # context["consumed"] = self.consumed
        context['my_consumed'] = FoodInstance.objects.filter(consumed__lte=today_end,
                                               consumed__gte=today_start)

        return context


class FoodInstanceDelete(DeleteView):
    model = FoodInstance
    success_url = reverse_lazy('index')


class DailyIntakeView(LoginRequiredMixin, generic.ListView):
    model = DailyIntake
    fields = '__all__'
    template_name = 'catalog/dailyintakelist.html'

class DailyIntakeUpdate(UpdateView):
    model = DailyIntake
    fields = '__all__'
    template_name = 'catalog/dailyintake_update_form.html'
    success_url=reverse_lazy('user-settings')

class NotesPageView(TemplateView):
    template_name = 'catalog/notes.html'
