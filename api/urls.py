from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view

from api import views

documentation = get_swagger_view(title='Products API')

urlpatterns = [
    url(r'^$', documentation),
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^products/(?P<id>.+)/$', views.ProductListByID.as_view()),
    url(r'^product-types/$', views.ProductTypeList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

