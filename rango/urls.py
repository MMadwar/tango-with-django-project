from django.urls import path
from rango import views


app_name = 'rango'


urlpatterns = [
        path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
]
#lines 12,13, sourced from the git provided in chapter 7
#https://github.com/tangowithcode/tango_with_django_2_code/tree/b90fc0b52abda784e09fd8ee99c9f7d356e54470/tango_with_django_project

