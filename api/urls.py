#api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, CreateDistrictView

urlpatterns = {
    url(r'^playerlist/$', CreateView.as_view(), name="create"),
    url(r'^playerlist/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    url(r'^districtlist/$', CreateDistrictView.as_view(), name="create_district")
}

urlpatterns = format_suffix_patterns(urlpatterns)