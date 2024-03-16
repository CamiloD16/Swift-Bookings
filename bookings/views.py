from django.shortcuts import render
from django.views.generic import View
from .models import Book

class BookingListView(View):
  def get(self, request, *args, **kwargs):
    books = Book.objects.all()
    context = {
      'books': books,
    }
    return render(request, "bookings/bookings.html", context)
