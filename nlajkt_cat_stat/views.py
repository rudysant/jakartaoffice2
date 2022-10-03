from cProfile import label
from django.http import HttpResponse
from django.db.models import Count, Q, Max
from django.template import loader
from .models import Catalogues
import datetime
from django.shortcuts import render
from django.views.generic import ListView
today = datetime.date.today()
thisyear = datetime.date.today().year
thismonth = datetime.date.today().month

def home(request):
    return render(request, 'base.html')

def cat_stat(request):
    curcons = Catalogues.objects.aggregate(Max('consignment_no')).get('consignment_no__max')
    bookcount = Catalogues.objects.all().count()    
    catyear = Catalogues.objects.filter(entry_date__year=thisyear).count()
    catmonth = Catalogues.objects.filter(entry_date__month=thismonth).count()
    catt = Catalogues.objects.filter(entry_date=today).count()
    catcons = Catalogues.objects.filter(consignment_no = curcons).count()
    
    context = {
        
        'catyear' : catyear,
        'catt' : catt,
        'bookcount' : bookcount,
        'catmonth' : catmonth,
        'curcons' : curcons,
        'catcons' : catcons,
      }
    
    template = loader.get_template('cat_stat.html')
    return HttpResponse(template.render(context, request))

class SearchResultsView(ListView):
    model = Catalogues
    template_name = 'search_result.html'
    paginate_by = 10
    
    def get_queryset(self):
        query1 = self.request.GET.get('q1')
        query2 = self.request.GET.get('q2')
        object_list = Catalogues.objects.filter(
          Q(entry_date__gte=query1)&Q(entry_date__lte=query2)
            )
        return object_list






def acq_stat(request):
    return render(request, 'acq_stat.html')
