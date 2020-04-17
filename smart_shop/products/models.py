from django.db import models
from django.utils.text import slugify
from django.conf import settings

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()
    
    def get_related(self,intance):
        first_product = self.get_queryset().filter(categories__in=intance.categories.all())
        second_product = self.get_queryset().filter(default=intance.default)
        pp = (first_productt | second_product).exclude(id=intance.id).distinct()
        return pp

class Product(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField('SubCategory', blank=True)

    class Meta:
        ordering = ["-title"]


    def __str_(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, editable=False,)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


# class MyModel(models.Model):
#     name = models.CharField()
#     slug = models.SlugField(unique=True, null=False)
#     def _generate_unique_slug(self)
#         unique_slug = slugify(self.name)
#         num = 1
#         while MyModel.objects.filter(slug=unique_slug).exists():
#             slug = '{}-{}'.format(unique_slug, num)
#             num += 1
#             return unique_slug
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = self._get_unique_slug()
#         super().save(*args, **kwargs)

        
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




class Variation(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(null=True, blank=True)

    def __srt__(self):
        return self.title

    def get_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else:
            return self.price