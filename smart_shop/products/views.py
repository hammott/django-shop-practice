from django.shortcuts import render
from rest_framework import generics
from django.views.generic.list import ListView

from . import serializers
from . import models
from . import pagination


# API VIEW ------------------------------------------
class CategoryListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = pagination.CategoryPagination

class SubCategoryListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.SubCategorySerializer
    pagination_class = pagination.SubCategoryPagination

# templates
class CategoryListView(ListView):
    model = models.Category
    queryset = models.Category.objects.all()
    template_name = "products/category_list.html"




class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProdcutDetailSerializer