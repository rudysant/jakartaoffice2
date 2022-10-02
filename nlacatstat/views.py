from cProfile import label
from django.http import HttpResponse
from django.db.models import Count, Q, Max
from django.template import loader
from .models import Catalogues
import datetime
from django.shortcuts import render
#from django.db.models import Q
from django.views.generic import ListView
today = datetime.date.today()
thisyear = datetime.date.today().year
thismonth = datetime.date.today().month


def index(request):
    curcons = Catalogues.objects.aggregate(Max('consignment_no')).get('consignment_no__max')
    mycatalogue = Catalogues.objects.all().values()
    bookcount = Catalogues.objects.all().count()
    pubyear = Catalogues.objects.values('publish_year').order_by('-publish_year').annotate(pubyearcount=Count('publish_year'))
    typepub = Catalogues.objects.values('publisher_type').annotate(typepubcount=Count('publisher_type'))
    typegenre = Catalogues.objects.values('genre').annotate(typegenrecount=Count('genre'))
    lang = Catalogues.objects.values('language').annotate(langcount=Count('language'))
    subj =Catalogues.objects.values('subject').annotate(subjcount=Count('subject'))
    typework = Catalogues.objects.values('work_type').annotate(worktypecount=Count('work_type'))
    vols = Catalogues.objects.values('volume').annotate(volcount=Count('volume'))
    copycat = Catalogues.objects.values('copycat').annotate(copycatcount=Count('copycat'))
    typeaut = Catalogues.objects.values('authorship_type').annotate(typeautcount=Count('authorship_type'))
    isbn = Catalogues.objects.values('ISBN').annotate(isbncount=Count('ISBN'))
    booksize = Catalogues.objects.values('size').annotate(sizecount=Count('size'))
        
    catyear = Catalogues.objects.filter(entry_date__year=thisyear).count()
    catmonth = Catalogues.objects.filter(entry_date__month=thismonth).count()
    catt = Catalogues.objects.filter(entry_date=today).count()
    catcons = Catalogues.objects.filter(consignment_no = curcons).count()
    
    context = {
        'mycatalogue' : mycatalogue,
        'pubyear' : pubyear,
        'typepub' : typepub,
        'typegenre' : typegenre,
        'lang' : lang,
        'subj' : subj,
        'typework' : typework,
        'typeaut' : typeaut,          
        'bookcount' : bookcount,
        'catyear' : catyear,
        'catt' : catt,
        'vols' : vols,
        'isbn' : isbn,
        'booksize' : booksize,
        'catmonth' : catmonth,
        'curcons' : curcons,
        'copycat' : copycat,
        'catcons' : catcons,
      }
    
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def detail_pubyear(request, publish_year):
    detail_pubyear = Catalogues.objects.all().filter(publish_year=publish_year)
    template = loader.get_template('detail_publishyear.html')
    context = {
    'detail_pubyear' : detail_pubyear,

  }
    return HttpResponse(template.render(context, request))

def detail_publisher(request, publisher_type):
  detail_pub = Catalogues.objects.all().filter(publisher_type=publisher_type)

  template = loader.get_template('detail_publisher.html')
  context = {
    'detail_pub' : detail_pub,
  }
  return HttpResponse(template.render(context, request))


def detail_genre(request, genre):
  detail_genre = Catalogues.objects.all().filter(genre=genre)

  template = loader.get_template('detail_genre.html')
  context = {
    'detail_genre' : detail_genre,
  }
  return HttpResponse(template.render(context, request))

def detail_language(request, language):
  detail_language = Catalogues.objects.all().filter(language=language)

  template = loader.get_template('detail_language.html')
  context = {
    'detail_language' : detail_language,
  }
  return HttpResponse(template.render(context, request))

def detail_subject(request, subject):
  detail_subject = Catalogues.objects.all().filter(subject=subject)

  template = loader.get_template('detail_subject.html')
  context = {
    'detail_subject' : detail_subject,
  }
  return HttpResponse(template.render(context, request))

def detail_worktypes(request, work_type):
  detail_worktypes= Catalogues.objects.all().filter(work_type=work_type)

  template = loader.get_template('detail_worktype.html')
  context = {
    'detail_worktypes' : detail_worktypes,
  }
  return HttpResponse(template.render(context, request))

def detail_volume(request, volume):
  detail_volumes= Catalogues.objects.all().filter(volume=volume)

  template = loader.get_template('detail_volume.html')
  context = {
    'detail_volumes' : detail_volumes,
  }
  return HttpResponse(template.render(context, request))

def detail_copycat(request, copycat):
  detail_copycats= Catalogues.objects.all().filter(copycat=copycat)

  template = loader.get_template('detail_copycat.html')
  context = {
    'detail_copycats' : detail_copycats,
  }
  return HttpResponse(template.render(context, request))

def detail_size(request, size):
  detail_sizes= Catalogues.objects.all().filter(size=size)

  template = loader.get_template('detail_size.html')
  context = {
    'detail_sizes' : detail_sizes,
  }
  return HttpResponse(template.render(context, request))

def detail_ISBN(request, ISBN):
  detail_ISBNs= Catalogues.objects.all().filter(ISBN=ISBN)

  template = loader.get_template('detail_isbn.html')
  context = {
    'detail_ISBNs' : detail_ISBNs,
  }
  return HttpResponse(template.render(context, request))


def detail_authorship(request, authorship_type):
  detail_aut = Catalogues.objects.all().filter(authorship_type=authorship_type)

  template = loader.get_template('detail_authorship.html')
  context = {
    'detail_aut': detail_aut,
  }
  return HttpResponse(template.render(context, request))


def yearpublish_chart(request):
  labels = []
  data = []

  queryset = Catalogues.objects.values('publish_year').order_by('-publish_year').annotate(langcount=Count('publish_year'))
  for xlang in queryset:
    labels.append(xlang['publish_year'])
    data.append(xlang['langcount'])

  return render(request, 'chart_yearpublish.html',{
    'labels' : labels,
    'data' : data,
    
  })

def publisher_chart(request):
  labels = []
  data = []

  queryset = Catalogues.objects.values('publisher_type').annotate(langcount=Count('publisher_type'))
  for xlang in queryset:
    labels.append(xlang['publisher_type'])
    data.append(xlang['langcount'])

  return render(request, 'chart_typepublish.html',{
    'labels' : labels,
    'data' : data,
  })

def genre_chart(request):
  labels = []
  data = []

  queryset = Catalogues.objects.values('genre').annotate(langcount=Count('genre'))
  for xlang in queryset:
    labels.append(xlang['genre'])
    data.append(xlang['langcount'])

  return render(request, 'chart_genre.html',{
    'labels' : labels,
    'data' : data,
  })

def language_chart(request):
  labels = []
  data = []

  queryset = Catalogues.objects.values('language').annotate(langcount=Count('language'))
  for xlang in queryset:
    labels.append(xlang['language'])
    data.append(xlang['langcount'])

  return render(request, 'chart_language.html',{
    'labels' : labels,
    'data' : data,
  })

def typeofwork_chart(request):
  labels = []
  data = []

  queryset = Catalogues.objects.values('work_type').annotate(langcount=Count('work_type'))
  for xlang in queryset:
    labels.append(xlang['work_type'])
    data.append(xlang['langcount'])

  return render(request, 'chart_typeofwork.html',{
    'labels' : labels,
    'data' : data,
  })

def copycat_chart(request):
  labels = []
  data = []

  queryset = Catalogues.objects.values('copycat').annotate(langcount=Count('copycat'))
  for xlang in queryset:
    labels.append(xlang['copycat'])
    data.append(xlang['langcount'])

  return render(request, 'chart_copycat.html',{
    'labels' : labels,
    'data' : data,
  })

def volume_chart(request):
  labels = []
  data = []

  queryset = Catalogues.objects.values('volume').annotate(langcount=Count('volume'))
  for xlang in queryset:
    labels.append(xlang['volume'])
    data.append(xlang['langcount'])

  return render(request, 'chart_volume.html',{
    'labels' : labels,
    'data' : data,
  })

def isbn_chart(request):
  labels = []
  data = []

  queryset = Catalogues.objects.values('ISBN').annotate(langcount=Count('ISBN'))
  for xlang in queryset:
    labels.append(xlang['ISBN'])
    data.append(xlang['langcount'])

  return render(request, 'chart_isbn.html',{
    'labels' : labels,
    'data' : data,
  })

def size_chart(request):
  labels = []
  data = []

  queryset = Catalogues.objects.values('size').annotate(langcount=Count('size'))
  for xlang in queryset:
    labels.append(xlang['size'])
    data.append(xlang['langcount'])

  return render(request, 'chart_size.html',{
    'labels' : labels,
    'data' : data,
  })

def authorship_chart(request):
  labels = []
  data = []

  queryset = Catalogues.objects.values('authorship_type').annotate(langcount=Count('authorship_type'))
  for xlang in queryset:
    labels.append(xlang['authorship_type'])
    data.append(xlang['langcount'])

  return render(request, 'chart_authorship.html',{
    'labels' : labels,
    'data' : data,
  })

def subject_chart(request):
  labels = []
  data = []

  queryset = Catalogues.objects.values('subject').annotate(langcount=Count('subject'))
  for xlang in queryset:
    labels.append(xlang['subject'])
    data.append(xlang['langcount'])

  return render(request, 'chart_subject.html',{
    'labels' : labels,
    'data' : data,
  })

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

