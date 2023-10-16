from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    content = RichTextField(verbose_name='Content')
    slug = models.CharField(unique=True, max_length=150, verbose_name='Friendly URL')
    order = models.IntegerField(default=0, verbose_name = 'Order')
    visible = models.BooleanField(verbose_name='Visible?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    
    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
    
    def __str__(self):
        return self.title