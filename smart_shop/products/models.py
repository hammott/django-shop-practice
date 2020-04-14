from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField('SubCategory', blank=True)

    class Meta:
        ordering = ["-title"]


    def __Srt__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __srt__(self):
        return self.title

class SubCategory(models.Model):
    category = models.ForeignKey('Category', 
                        related_name='subCategoryList', 
                        on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __srt__(self):
            return self.title

