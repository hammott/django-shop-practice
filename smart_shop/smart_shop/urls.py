"""smart_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework_swagger.views import get_swagger_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from . import views
from products.views import (
    CategoryListAPIView,
    CategoryRetrieveAPIView,


)


# schema_view = get_swagger_view(
#     title='RESTFUL API',
#     renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

schema_view = get_swagger_view(title='RESTFUL API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('user/', include('user.user_urls')),
    path('product/', include('products.urls')),

    path('api-swagger/',schema_view)

]


# API All
urlpatterns +=[
    path('login/user', views.login, name='login'),
    path('api/categories/',CategoryListAPIView.as_view(), name='categories_api'),
    path('api/categories/(?P<pk>\d+)/',CategoryRetrieveAPIView.as_view(), name='category_detail_api'),
]



