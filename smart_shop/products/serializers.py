from rest_framework import serializers
from rest_framework import generics
from .models import (
                    Category, 
                    Product, 
                    Variation, 
                    SubCategoryFirst,
                    SubCategorySecond
                    )


# For Varation Model ------------------------------------------------
class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = [
            "id",
            "title",
            "price"
        ]


# For Product Model -----------------------------------------------
class ProductDetailUpdateSerializer(serializers.ModelSerializer):
    set_variation = VariationSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields =[
            "id",
            "title",
            "short_description",
            "price",
            "image",
            "set_variation",
        ]


    def get_image(self,obj):
        try:
            return obj.productimage_set.first().image.url
        except:
            return None
    
    def create(self,validated_data):
        title = validated_data["title"]
        Product.objects.get(title=title)
        product = Product.objects.create(**validated_data)
        return product
    
    def update(self, instance, validated_data):
        instance.title = validated_data["title"]
        instance.save()
        return instance


class ProdcutDetailSerializer(serializers.ModelSerializer):
    set_variation = VariationSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields =[
            "id",
            "title",
            "short_description",
            "price",
            "image",
            "set_variation",
        ]

    def get_image(self,obj):
        return obj.productimage_set.first().image.url

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name ='products_detail_api')
    set_variation = VariationSerializer(many=True)
    image = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields =[
            "url",
            "id",
            "title",
            "short_description",
            "price",
            "image",
            "set_variation",
        ]
    def get_image(self,obj):
        try:
            return obj.productimage_set.first().image.url
        except:
            return None

# Category -----------------------------------------------

class CategorySerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(
#                             view_name='category_detail_api',
#                             many=True,
#                             read_only=True,
#                             )
#     set_product = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields =[
            # "url",
            "id",
            "title",
            "description",
            "timestamp",
            # "set_product",
        ]



# SubCategory -------------------------------------------
class SubCategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
                            view_name='subcategory_detail_api')
    set_product = ProductSerializer(many=True)
    class Meta:
        model = SubCategoryFirst
        fields =[
            "url",
            "id",
            "title",
            "timestamp",
            "set_product",
        ]
