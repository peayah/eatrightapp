from django import forms
from datetime import *
import uuid
from catalog.models import FoodInstance, Food
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy


# class ConsumeFoodForm(forms.Form):
class ConsumeFoodForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(ConsumeFoodForm, self).__init__(*args, **kwargs)
        self.fields['food'].queryset = Food.objects.filter(kind="x")
        self.fields['food'].label = "Extra"

    class Meta:
        model = FoodInstance
        # fields = ('food', 'eater',)
        fields = ('food', )


class ConsumeBreadForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConsumeBreadForm, self).__init__(*args, **kwargs)
        self.fields['food'].queryset = Food.objects.filter(kind="b")
        self.fields['food'].label = "Bread"

    class Meta:
        model = FoodInstance
        # fields = ('food', 'eater',)
        fields = ('food',)


class ConsumeFruitForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConsumeFruitForm, self).__init__(*args, **kwargs)
        self.fields['food'].queryset = Food.objects.filter(kind="f")
        self.fields['food'].label = "Fruit"

    class Meta:
        model = FoodInstance
        # fields = ('food', 'eater',)
        fields = ('food',)


class ConsumeMeatForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConsumeMeatForm, self).__init__(*args, **kwargs)
        self.fields['food'].queryset = Food.objects.filter(kind="m")
        self.fields['food'].label = "Meat"

    class Meta:
        model = FoodInstance
        # fields = ('food', 'eater',)
        fields = ('food',)


class ConsumeGreensForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConsumeGreensForm, self).__init__(*args, **kwargs)
        self.fields['food'].queryset = Food.objects.filter(kind="g")
        self.fields['food'].label = "Greens"

    class Meta:
        model = FoodInstance
        # fields = ('food', 'eater',)
        fields = ('food',)


class ConsumeWaterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConsumeWaterForm, self).__init__(*args, **kwargs)
        self.fields['food'].queryset = Food.objects.filter(kind="w")
        self.fields['food'].label = "Water"

    class Meta:
        model = FoodInstance
        # fields = ('food', 'eater',)
        fields = ('food',)


class ConsumeCaffeineForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConsumeCaffeineForm, self).__init__(*args, **kwargs)
        self.fields['food'].queryset = Food.objects.filter(kind="c")
        self.fields['food'].label = "Caffeine"

    class Meta:
        model = FoodInstance
        # fields = ('food', 'eater',)
        fields = ('food',)


class ConsumeOilForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConsumeOilForm, self).__init__(*args, **kwargs)
        self.fields['food'].queryset = Food.objects.filter(kind="o")
        self.fields['food'].label = "Oil"

    class Meta:
        model = FoodInstance
        # fields = ('food', 'eater',)
        fields = ('food',)
