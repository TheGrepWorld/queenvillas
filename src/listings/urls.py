from django.urls import path
from .views import listing_page,listing_detail
urlpatterns = [
    path('', listing_page, name="listingHome"),
    path("<str:slug>", listing_detail, name="listingDetail"),
]