from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'about/', views.about, name='about'),
    url(r'page/', views.show_page, name='page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', 
        views.show_category, name='show_category'),
]
