from django.contrib import admin
from .models import Product, Category, SubCategory, Variation
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class VariationInLine(admin.TabularInline):
	model=Variation
	extra = 0
	max_num = 10


class ProductAdmin(admin.ModelAdmin):
	list_display = ['title', 'price']
	inlines =[VariationInLine]
	
	class Meta:
		model = Product

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',), }
	class Meta:
		model= Category

admin.site.register(Product,ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory)
