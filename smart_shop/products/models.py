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
    categories = models.OneToOneField('SubCategorySecond', blank=True, on_delete=models.CASCADE, null=True)

    objects = ProductManager()

    class Meta:
        ordering = ["-title"]


    def __str_(self):
        return self.title

    def get_absolute_url(self):
        return "product_detail/%i/" % self.id
    
    def get_image_url(self):
        img = self.productimage_set.first()
        if img:
            return img.image.url
        return img



class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})
    
        
class SubCategoryFirst(models.Model):
    category = models.ForeignKey('Category', 
                        related_name='subCategoryFirstList', 
                        on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
            return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class SubCategorySecond(models.Model):
    category = models.ForeignKey('SubCategoryFirst', 
                        related_name='subCategorySecondList', 
                        on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
            return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

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

def image_upload_to(instance, filename):
	title = instance.product.title
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
	return "products/images/%s/%s" %(slug, new_filename)




class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=image_upload_to)

	def __str__(self):
		return self.product.title


