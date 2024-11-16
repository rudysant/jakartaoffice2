from django.urls import path
from . import views
from .views import SearchResultsView, SearchResultsView2

urlpatterns = [
    path('', views.home, name = 'home'),
 #   path('cat_stat/', views.cat_stat, name='cat_stat'),
 #   path('acq_stat/', views.acq_stat, name='acq_stat'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search_/', SearchResultsView2.as_view(), name='search_title_results'),

    path('detail_pubyear/<int:publish_year>/', views.detail_pubyear, name='detail_pubyear'),
    path('detail_publisher/<str:publisher_type>/', views.detail_publisher, name='detail_publisher'),
    path('detail_genre/<str:genre>/', views.detail_genre, name='detail_genre'),
    path('detail_language/<str:language>/', views.detail_language, name='detail_language'),
    path('detail_authorship/<str:authorship_type>/', views.detail_authorship, name='detail_authorship'),
    path('detail_copycat/<str:copycat>/', views.detail_copycat, name='detail_copycat'),
    path('detail_subject/<str:subject>/', views.detail_subject, name='detail_subject'),

    path('cat_stat/yearpublish-chart/', views.yearpublish_chart, name='yearpublish-chart'),
    path('cat_stat/publisher-chart/', views.publisher_chart, name='publisher-chart'),
    path('cat_stat/genre-chart/', views.genre_chart, name='genre-chart'),
    path('cat_stat/language-chart/', views.language_chart, name='language-chart'),
    path('cat_stat/authorship-chart/', views.authorship_chart, name='authorship-chart'),
    path('cat_stat/copycat-chart/', views.copycat_chart, name='copycat-chart'),
    path('cat_stat/subject-chart/', views.subject_chart, name='subject-chart'),
 #   path('books/', views.book_list, name='book_list'),
]