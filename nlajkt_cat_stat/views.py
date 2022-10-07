from cProfile import label
from mimetypes import suffix_map
from django.http import HttpResponse
from django.db.models import Count, Q, Max, Sum
from django.template import loader
from .models import Catalogues, Acquisition
import datetime
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator

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
    pubyear = Catalogues.objects.values('publish_year').order_by('-publish_year').annotate(pubyearcount=Count('publish_year'))
    typepub = Catalogues.objects.values('publisher_type').annotate(typepubcount=Count('publisher_type'))
    typegenre = Catalogues.objects.values('genre').annotate(typegenrecount=Count('genre'))
    lang = Catalogues.objects.values('language').annotate(langcount=Count('language'))
    typeaut = Catalogues.objects.values('authorship_type').annotate(typeautcount=Count('authorship_type'))

    context = {
        'catyear' : catyear,
        'catt' : catt,
        'bookcount' : bookcount,
        'catmonth' : catmonth,
        'curcons' : curcons,
        'catcons' : catcons,
        'pubyear' : pubyear,
        'typepub' : typepub,
        'typegenre' : typegenre,
        'lang' : lang,
        'typeaut' : typeaut,
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

def detail_pubyear(request, publish_year):
    detail_pubyear = Catalogues.objects.all().filter(publish_year=publish_year)
    page = request.GET.get('page', 1)
    paginator = Paginator(detail_pubyear, 10)
    try:
        paging = paginator.page(page)
    except PageNotAnInteger:
        paging = paginator.page(1)
    except EmptyPage:
        paging = paginator.page(paginator.num_pages)
    template = loader.get_template('detail_publishyear.html')
    context = {'paging' : paging,}
    return HttpResponse(template.render(context, request))

def detail_publisher(request, publisher_type):
    detail_pub = Catalogues.objects.all().filter(publisher_type=publisher_type)
    page = request.GET.get('page', 1)
    paginator = Paginator(detail_pub, 10)
    try:
        paging = paginator.page(page)
    except PageNotAnInteger:
        paging = paginator.page(1)
    except EmptyPage:
        paging = paginator.page(paginator.num_pages)
    template = loader.get_template('detail_publisher.html')
    context = {'paging' : paging,}
    return HttpResponse(template.render(context, request))

def detail_genre(request, genre):
    detail_genre = Catalogues.objects.all().filter(genre=genre)
    page = request.GET.get('page', 1)
    paginator = Paginator(detail_genre, 10)
    try:
        paging = paginator.page(page)
    except PageNotAnInteger:
        paging = paginator.page(1)
    except EmptyPage:
        paging = paginator.page(paginator.num_pages)
    template = loader.get_template('detail_genre.html')
    context = {'paging' : paging,}
    return HttpResponse(template.render(context, request))

def detail_language(request, language):
    detail_language = Catalogues.objects.all().filter(language=language)
    page = request.GET.get('page', 1)
    paginator = Paginator(detail_language, 10)
    try:
        paging = paginator.page(page)
    except PageNotAnInteger:
        paging = paginator.page(1)
    except EmptyPage:
        paging = paginator.page(paginator.num_pages)
    template = loader.get_template('detail_language.html')
    context = {'paging' : paging,}
    return HttpResponse(template.render(context, request))

def detail_authorship(request, authorship_type):
    detail_authorship = Catalogues.objects.all().filter(authorship_type=authorship_type)
    page = request.GET.get('page', 1)
    paginator = Paginator(detail_authorship, 10)
    try:
        paging = paginator.page(page)
    except PageNotAnInteger:
        paging = paginator.page(1)
    except EmptyPage:
        paging = paginator.page(paginator.num_pages)
    template = loader.get_template('detail_authorship.html')
    context = {'paging' : paging,}
    return HttpResponse(template.render(context, request))

def yearpublish_chart(request):
    labels = []
    data = []
    queryset = Catalogues.objects.values('publish_year').order_by('-publish_year').annotate(langcount=Count('publish_year'))
    for xlang in queryset:
      labels.append(xlang['publish_year'])
      data.append(xlang['langcount'])
    return render(request, 'chart_yearpublish.html',{'labels' : labels,'data' : data,})

def publisher_chart(request):
    labels = []
    data = []
    queryset = Catalogues.objects.values('publisher_type').annotate(langcount=Count('publisher_type'))
    for xlang in queryset:
      labels.append(xlang['publisher_type'])
      data.append(xlang['langcount'])
    return render(request, 'chart_typepublish.html',{'labels' : labels,'data' : data,})

def genre_chart(request):
    labels = []
    data = []
    queryset = Catalogues.objects.values('genre').annotate(langcount=Count('genre'))
    for xlang in queryset:
      labels.append(xlang['genre'])
      data.append(xlang['langcount'])
    return render(request, 'chart_genre.html',{'labels' : labels,'data' : data,})

def language_chart(request):
    labels = []
    data = []
    queryset = Catalogues.objects.values('language').annotate(langcount=Count('language'))
    for xlang in queryset:
      labels.append(xlang['language'])
      data.append(xlang['langcount'])
    return render(request, 'chart_language.html',{'labels' : labels,'data' : data,})

def authorship_chart(request):
    labels = []
    data = []
    queryset = Catalogues.objects.values('authorship_type').annotate(langcount=Count('authorship_type'))
    for xlang in queryset:
      labels.append(xlang['authorship_type'])
      data.append(xlang['langcount'])
    return render(request, 'chart_authorship.html',{'labels' : labels,'data' : data,})



def acq_stat(request):
    acq = Acquisition.objects.all()
    curcons = Catalogues.objects.aggregate(Max('consignment_no')).get('consignment_no__max')
    total_proc = Acquisition.objects.aggregate(Sum('titles_proc')).get('titles_proc__sum')
    bookcount = Catalogues.objects.all().count()

    vendor_count = Acquisition.objects.values('vendor').annotate(vendorcount=Sum('titles_proc'))

    context = {
        'acq' : acq,
        'curcons' : curcons,
        'total_proc' : total_proc,
        'bookcount' : bookcount,
        'vendor_count' : vendor_count
    }
    template = loader.get_template('acq_stat.html')
    return HttpResponse(template.render(context, request))
