from django.shortcuts import render
from django.views.generic import View
from .models import Book, Category

class BookingListView(View):
  def get(self, request, *args, **kwargs):
    books = Book.objects.all()
    context = {
      'books': books,
    }
    return render(request, "bookings/bookings.html", context)

class GalleryListView(View):
  def get(self, request, category=None, *args, **kwargs):

    books = Book.objects.all()
    categories = Category.objects.all()[:6]
    category_name = None

    if category:
      books = books.filter(category__name__iexact=category)
      category_name = Category.objects.get(name__iexact=category).name

    context = {
      'books': books,
      'categories': categories,
      'category_name': category_name
    }

    template = "bookings/gallery_all.html"

    if category:
      template = "bookings/gallery.html"

    return render(request, template, context)
