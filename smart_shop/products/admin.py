from django.contrib import admin
from .models import Product, Category, SubCategory
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class ProductAdmin(admin.ModelAdmin):
	list_display = ['title', 'price']
	class Meta:
		model = Product

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
