from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import product_list, product_detail, category_list, product_filter

urlpatterns = {
    url(r'^list/$', product_list),
    url(r'^list/(?P<pk>[0-9]+)/$', product_detail),
    url(r'^filter/(?P<param>\w{0,50})/$', product_filter),
    url(r'^category/$', category_list),
}

urlpatterns = format_suffix_patterns(urlpatterns)