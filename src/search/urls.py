from django.urls import path, re_path

from .views import (SearchProductView)

urlpatterns = [

    path('', SearchProductView.as_view(), name='query'),

    # re_path('(?P<slug>[\w-]+)/', ProductDetailSlugView.as_view(),name='detail')

]


