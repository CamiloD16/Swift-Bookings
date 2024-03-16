from django.views.generic import View
from django.shortcuts import render, redirect
from bookings.models import Category

class HomeView(View):
  def get(self, request, *args, **kwargs):
    categories = Category.objects.all()[:6]
    context = {
      'categories': categories
    }
    return render(request, "home/home.html", context)