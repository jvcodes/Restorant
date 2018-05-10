from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import FormView
from .models import RestaurantLocation


class RestaurantView(DetailView):
      queryset=RestaurantLocation.objects.all()
