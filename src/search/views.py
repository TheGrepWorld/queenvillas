from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from residential.models import ResidentialDetails
from django.views.generic import ListView


class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        context['query_type'] = self.request.GET.get('q1')
        context['query_city'] = self.request.GET.get('q2')
        context['query_locality'] = self.request.GET.get('q3')
        context['query_bedroom'] = self.request.GET.get('q4')
        context['query_lower_price'] = self.request.GET.get('q5')
        context['query_upper_price'] = self.request.GET.get('q6')

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query1 = method_dict.get('q1', None)
        query2=method_dict.get('q2',None)
        query3 = method_dict.get('q3', None)
        query4=method_dict.get('q4', None)
        query5=method_dict.get('q5', None)
        query6=method_dict.get('q6', None)

        if query1 and query2 and query3 and query4 is not None:
            return ResidentialDetails.objects.search(query1,query2,query3,query4,query5,query6)
        return ResidentialDetails.objects.featured()

