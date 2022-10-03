from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.home, name = 'home'),
    path('cat_stat/', views.cat_stat, name='cat_stat'),
    path('acq_stat/', views.acq_stat, name='cat_stat'),
    path('/', SearchResultsView.as_view(), name='search_results'),
    
]