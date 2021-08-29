from django.urls import path, re_path
from .views import ResidentialListView, add_property, ResidentialDetailSlugView, get_filter_data

urlpatterns = [
    path('', ResidentialListView, name="residentiallistingHome"),
    path('filter', get_filter_data, name="residential-filter"),
    re_path('(?P<slug>[\w-]+)/', ResidentialDetailSlugView.as_view(), name='detail'),
    path('post-residential-property', add_property, name='add'),
    # path('resenditial-listing', ResidentialListView.as_view() , name='rlist')
]
