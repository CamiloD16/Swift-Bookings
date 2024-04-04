from django.urls import path
from .views import BookingListView, GalleryListView

app_name="bookings"


urlpatterns = [
  path("", BookingListView.as_view(), name="home"),
  path("gallery/<str:category>/", GalleryListView.as_view(), name="gallery"),
  path("gallery/", GalleryListView.as_view(), name="gallery_all"),
]