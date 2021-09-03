from django.urls import path, re_path
from .views import CommercialListView, CommercialDetails, CommercialDetailSlugView
urlpatterns = [
    path('', CommercialListView, name="commerciallistingHome"),
    re_path('(?P<slug>[\w-]+)/', CommercialDetailSlugView.as_view(), name='detail'),
    # path('post-commercial-property', add_property, name='add'),
]
