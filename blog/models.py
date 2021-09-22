from django.db import models
from django.db.models.deletion import CASCADE
from pages.models import STATUS
# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=100,verbose_name="Kateqoriya adı")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yaradıldığı tarix")

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"

class BlogModel(models.Model):
    title = models.CharField(max_length=100,verbose_name="Başlıq")
    category = models.ForeignKey(CategoryModel,on_delete=CASCADE,verbose_name="Kateqoriya")
    image = models.ImageField(upload_to = "blogphotos",verbose_name="Şəkil")
    text = models.TextField(verbose_name="Mətin")
    status = models.CharField(max_length=100, choices=STATUS)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yaradılma tarixi")

    def __str__(self):
        
        return self.title
    
    class Meta:
        verbose_name = "Bloq"
        verbose_name_plural = "Bloqlar"