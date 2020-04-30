from django.contrib import admin
from .models import (Product, 
					Category, 
					SubCategoryFirst,
					SubCategorySecond,
					Variation, 
					ProductImage,)
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class VariationInLine(admin.TabularInline):
	model=Variation
	extra = 0
	max_num = 10



class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0
	max_num = 10



class ProductAdmin(admin.ModelAdmin):
	list_display = ['title', 'price','active']
	inlines =[VariationInLine,ProductImageInline]
	
	class Meta:
		model = Product

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',), }
	class Meta:
		model= Category

class SubCategoryFirstAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('title',),}
	list_display=['title','category','active']
	class Meta:
		model= SubCategoryFirst

class SubCategorySecondAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('title',),}
	list_display=['title','category','active']
	class Meta:
		model= SubCategorySecond




admin.site.register(Product,ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategoryFirst, SubCategoryFirstAdmin)
admin.site.register(SubCategorySecond, SubCategorySecondAdmin)
admin.site.register(ProductImage)
