from rest_framework import serializers
from .models import (
                    Category, 
                    Product, 
                    Variation, 
                    SubCategory
                    )


# For Varation Model
class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = [
            "id",
            "title",
            "price"
        ]


