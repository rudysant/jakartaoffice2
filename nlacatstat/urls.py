from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.index, name='index'),
  
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('detail_pubyear/<int:publish_year>/', views.detail_pubyear, name='detail_pubyear'),
    path('detail_publisher/<str:publisher_type>/', views.detail_publisher, name='detail_publisher'),
    path('detail_language/<str:language>/', views.detail_language, name='detail_language'),
    path('detail_genre/<str:genre>/', views.detail_genre, name='detail_genre'),
    path('detail_subject/<str:subject>/', views.detail_subject, name='detail_subject'),
    path('detail_worktypes/<str:work_type>/', views.detail_worktypes, name='detail_worktypes'),
    path('detail_volume/<str:volume>/', views.detail_volume, name='detail_volume'),
    path('detail_copycat/<str:copycat>/', views.detail_copycat, name='detail_copycat'),
    path('detail_ISBN/<str:ISBN>/', views.detail_ISBN, name='detail_ISBN'),
    path('detail_size/<str:size>/', views.detail_size, name='detail_size'),
    path('detail_authorship/<str:authorship_type>/', views.detail_authorship, name='detail_authorship'),
    path('yearpublish-chart/', views.yearpublish_chart, name='yearpublish-chart'),
    path('publisher-chart/', views.publisher_chart, name='publisher-chart'),
    path('genre-chart/', views.genre_chart, name='genre-chart'),
    path('language-chart/', views.language_chart, name='language-chart'),
    path('typeofwork-chart/', views.typeofwork_chart, name='typeofwork-chart'),
    path('copycat-chart/', views.copycat_chart, name='copycat-chart'),
    path('volume-chart/', views.volume_chart, name='volumee-chart'),
    path('isbn-chart/', views.isbn_chart, name='isbn-chart'),
    path('size-chart/', views.size_chart, name='size-chart'),
    path('authorship-chart/', views.authorship_chart, name='authorship-chart'),
    path('subject-chart/', views.subject_chart, name='subject-chart'),
]