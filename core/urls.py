from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home" ),
    path("bookings/", include("bookings.urls", namespace="bookings")),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)