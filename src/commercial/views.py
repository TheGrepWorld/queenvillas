from django.http.response import Http404
from django.shortcuts import render

from .models import CommercialDetails
from django.views.generic import ListView, DetailView
from .forms import Filterform
from django.views.generic.edit import FormView
from django.db.models import Q


# from analytics.mixins import ObjectViewdMixin


def CommercialListView(request):
    type = request.GET.get('type')
    filter_form = Filterform()
    price = request.GET.get('price')
    selected_bhk = 0
    if type is not None and price is None:
        print("in if type", type)
        initial_dict = {
            "type": type
        }
        filter_form = Filterform(initial=initial_dict)
        object_list = CommercialDetails.objects.filter(property_type__iexact=type)

    elif price is not None and type is None:
        initial_dict = {
            "price": price

        }
        filter_form = Filterform(initial=initial_dict)
        print("in if price")
        if price == '3000000':
            object_list = CommercialDetails.objects.filter(expected_price__lte=price)
        if price == '5000000':
            print(price)
            object_list = CommercialDetails.objects.filter(expected_price__lte=price).filter(
                expected_price__gte=3000000)
        if price == '10000000':
            print(price)
            object_list = CommercialDetails.objects.filter(expected_price__lte=price).filter(
                expected_price__gte=5000000)
        if price == '100000001':
            object_list = CommercialDetails.objects.filter(expected_price__gte='10000000')
    elif price is not None and type is not None:
        initial_dict = {
            "price": price,
            "type": type

        }
        filter_form = Filterform(initial=initial_dict)
        print("in b and p")
        if price == '3000000':
            object_list = CommercialDetails.objects.filter(expected_price__lte=price).filter(bedrooms__iexact=type)
        if price == '5000000':
            print(price)
            object_list = CommercialDetails.objects.filter(expected_price__lte=price).filter(
                expected_price__gte=3000000).filter(bedrooms__iexact=type)
        if price == '10000000':
            print(price)
            object_list = CommercialDetails.objects.filter(expected_price__lte=price).filter(
                expected_price__gte=5000000).filter(bedrooms__iexact=type)
        if price == '100000001':
            object_list = CommercialDetails.objects.filter(expected_price__gte='10000000').filter(
                bedrooms__iexact=type)
    else:
        selected_bhk = 0
        print("kuch toh gadbad hai ")
        object_list = CommercialDetails.objects.all()
    context = {
        "selected_bhk": selected_bhk,
        "object_list": object_list,
        "filter_form": filter_form
    }
    return render(request, "commercial/list.html", context)


def get_filter_data(request):
    queryset = CommercialDetails.objects.none()
    if request.method == 'GET':
        bhks = request.GET.getlist('bhk')
        print(bhks)
        if bhks is not None:
            for i in bhks:
                queryset |= (CommercialDetails.objects.all().filter(bedrooms__iexact=i))
    print(queryset)

    context = {
        "data": queryset
    }
    return render(request, "residentials/resfilter.html", context)


class CommercialDetailSlugView(DetailView):
    queryset = CommercialDetails.objects.all()
    template_name = "residentials/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CommercialDetailSlugView, self).get_context_data(*args, **kwargs)
        request = self.request
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = CommercialDetails.objects.get(slug=slug)
        except CommercialDetails.DoesNotExist:
            raise Http404("Not Found....")
        except CommercialDetails.MultipleObjectsReturned:
            qs = CommercialDetails.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Uhhmm.. !")
        return instance
