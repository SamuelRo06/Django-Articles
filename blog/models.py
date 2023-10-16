from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.CharField(max_length=255, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    content = RichTextField(verbose_name='Content')
    image = models.ImageField(default='null', verbose_name='Image', upload_to='articles/list.html')
    public = models.BooleanField(verbose_name="Posted")
    user = models.ForeignKey(User, editable=False, verbose_name='User', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name='Categories', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    
    def __str__(self):
        return self.title