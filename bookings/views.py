from django.shortcuts import render
from django.views.generic import View


class BookingListView(View):
  def get(self, request, *args, **kwargs):
    context = {

    }
    return render(request, "bookings/bookings.html", context)
