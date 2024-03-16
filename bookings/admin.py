from django.contrib import admin
from .models import Book, Username, Rental, Category


admin.site.register(Username)
admin.site.register(Book)
admin.site.register(Rental)
admin.site.register(Category)
