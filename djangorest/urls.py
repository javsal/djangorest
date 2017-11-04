
from django.conf.urls import url, include
from django.contrib import admin
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^category/', include('category.urls')),
    url(r'^product/', include('product.urls')),
    url(r'^aggexe/', include('aggexe.urls')),
    url(r'^', include('api.urls')),
]
