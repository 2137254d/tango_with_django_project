from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'^(?P<page_views>[0-9]+)/$', views.show_page, name='show_page'),
    url(r'^add_category/$', views.add_category, name='add_category"'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', 
        views.show_category, name='show_category'),
]
