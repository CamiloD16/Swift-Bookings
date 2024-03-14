from django.contrib import admin
from .models import Book, Username, Rental


admin.site.register(Username)
admin.site.register(Book)
admin.site.register(Rental)
