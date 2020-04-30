from django.shortcuts import render
from rest_framework import generics
from django.views.generic.list import ListView
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from . import models
from . import pagination



class APIhomeView(APIView):
    def get(self, request, format=None):
        data={
            "categories": {
                "count": Category.objects.all().count(),
                "url": api_reverse("categories_api", request=request)
            },
        }
        return Response(data)
# API VIEW ------------------------------------------
class CategoryListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = pagination.CategoryPagination

class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

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