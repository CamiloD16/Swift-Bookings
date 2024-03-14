from django.db import models


class Username(models.Model):
    username = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank =True)
    address = models.CharField(max_length=100, blank =True)

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank =True)
    author = models.CharField(max_length=100, blank =True)
    publication_year = models.PositiveIntegerField(blank =True)

    def __str__(self):
        return self.title

class Rental(models.Model):
    user = models.ForeignKey(Username, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('returned', 'returned'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} rented {self.book.title}"

    def __str__(self):
        return self.user.username
