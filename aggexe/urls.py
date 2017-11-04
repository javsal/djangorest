from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import agg_query

urlpatterns = {
    url(r'^aggpractice/$', agg_query),
}

urlpatterns = format_suffix_patterns(urlpatterns)
