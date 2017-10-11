from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductCategoryList

urlpatterns = {
    url(r'^categorylist/$', ProductCategoryList.as_view(), name='category-list')
}

urlpatterns = format_suffix_patterns(urlpatterns)