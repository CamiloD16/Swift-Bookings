from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home" ),
    path("bookings/", include("bookings.urls", namespace="bookings")),
    path("__reload__/", include("django_browser_reload.urls")),
]
