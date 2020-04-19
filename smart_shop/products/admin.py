from django.contrib import admin
from .models import Product, Category, SubCategory, Variation, ProductImage
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

class SubCategoryAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('title',),}
	class Meta:
		model= SubCategory




admin.site.register(Product,ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(ProductImage)
