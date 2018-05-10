from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import FormView,DetailView
from .models import RestaurantLocation
from django import forms
from django.forms import ModelForm

class RestaurantCreateView(forms.Form):
    name        =forms.CharField()
    location    =forms.CharField()
    category    =forms.CharField()

    def clean_name(self):
        name=self.cleaned_data.get('name')
        if name=='hello':
            raise forms.ValidationError("not valid name")
        return name

class RestaurantView(DetailView):
      queryset=RestaurantLocation.objects.all()

class RestaurantLocationCreateForm(ModelForm):
    class Meta:
        model=RestaurantLocation
        fields=['name','location','category']

    def clean_name(self):
        name=self.cleaned_data.get('name')
        if name=='hello':
            raise forms.ValidationError("not valid name")
        return name
