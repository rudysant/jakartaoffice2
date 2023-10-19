from django.shortcuts import render
from .models import Catalogues, Consignment, Cat_cons, BookRev
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.template import loader
from django.http import HttpResponse
import datetime

today = datetime.date.today()
thisyear = datetime.date.today().year
thismonth = datetime.date.today().month

one_week_ago = datetime.date.today() - datetime.timedelta(days=7)
oldyear = thisyear-10

def home(request):
    bookcount = Catalogues.objects.all().count()
    catt = Catalogues.objects.filter(entry_date=today).count()
    catweek = Catalogues.objects.filter(entry_date__gte=one_week_ago).count()
#    catmonth = Catalogues.objects.filter(entry_date__month = thismonth).count()
    catmonth = Catalogues.objects.filter(entry_date__month=thismonth).count()
    catyear = Catalogues.objects.filter(entry_date__year=thisyear).count()
    curcons = Consignment.objects.filter(status = 'In process').only('consign_no')[0].consign_no
    catcons = Catalogues.objects.filter(consignment_no = curcons).count()
    cat_cons = Cat_cons.objects.all().order_by('-consign_no')
    pubyear = Catalogues.objects.values('publish_year').order_by('-publish_year').annotate(pubyearcount=Count('publish_year'))
    typepub = Catalogues.objects.values('publisher_type').annotate(typepubcount=Count('publisher_type'))
    typegenre = Catalogues.objects.values('genre').annotate(typegenrecount=Count('genre'))
    lang = Catalogues.objects.values('language').annotate(langcount=Count('language'))
    typeaut = Catalogues.objects.values('authorship_type').annotate(typeautcount=Count('authorship_type'))
    copycat = Catalogues.objects.values('copycat').annotate(copycatcount=Count('copycat'))
    subj =Catalogues.objects.values('subject').annotate(subjcount=Count('subject'))
    oldpub = Catalogues.objects.filter(publish_year__lt = oldyear).count()
    bookrev = BookRev.objects.all().order_by('-id')

    context = {
        'catyear' : catyear,
        'catt' : catt,
        'catweek' : catweek,
        'bookcount' : bookcount,
        'catmonth' : catmonth,
        'curcons' : curcons,
        'catcons' : catcons,
        'cat_cons' : cat_cons,
        'pubyear' : pubyear,
        'oldpub' : oldpub,
        'typepub' : typepub,
        'typegenre' : typegenre,
        'lang' : lang,
        'typeaut' : typeaut,
        'copycat' : copycat,
        'subj' : subj,
        'bookrev' : bookrev,

    }

    return render(request, 'base.html', context)

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

class SearchResultsView2(ListView):
    model = Catalogues
    template_name = 'search_title_result.html'
    paginate_by = 10

    def get_queryset(self):
        query1 = self.request.GET.get('q1')
        query2 = self.request.GET.get('q2')
        object_list = Catalogues.objects.filter(
          Q(title__contains=query1)&Q(title__contains=query2)
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

def detail_copycat(request, copycat):
    detail_copycat = Catalogues.objects.all().filter(copycat=copycat)
    page = request.GET.get('page', 1)
    paginator = Paginator(detail_copycat, 10)
    try:
        paging = paginator.page(page)
    except PageNotAnInteger:
        paging = paginator.page(1)
    except EmptyPage:
        paging = paginator.page(paginator.num_pages)
    template = loader.get_template('detail_copycat.html')
    context = {'paging' : paging,}
    return HttpResponse(template.render(context, request))

def detail_subject(request, subject):
    detail_subject = Catalogues.objects.all().filter(subject=subject)
    page = request.GET.get('page', 1)
    paginator = Paginator(detail_subject, 10)
    try:
        paging = paginator.page(page)
    except PageNotAnInteger:
        paging = paginator.page(1)
    except EmptyPage:
        paging = paginator.page(paginator.num_pages)
    template = loader.get_template('detail_subject.html')
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

def copycat_chart(request):
    labels = []
    data = []
    queryset = Catalogues.objects.values('copycat').annotate(langcount=Count('copycat'))
    for xlang in queryset:
      labels.append(xlang['copycat'])
      data.append(xlang['langcount'])
    return render(request, 'chart_copycat.html',{'labels' : labels,'data' : data,})

def subject_chart(request):
    labels = []
    data = []
    queryset = Catalogues.objects.values('subject').annotate(langcount=Count('subject'))
    for xlang in queryset:
      labels.append(xlang['subject'])
      data.append(xlang['langcount'])
    return render(request, 'chart_subject.html',{'labels' : labels,'data' : data,})





