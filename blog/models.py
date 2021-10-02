from django.db import models
from django.db.models.deletion import CASCADE
from pages.models import STATUS
from taggit.managers import TaggableManager

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=100,verbose_name="Kateqoriya adı")
    slug = models.SlugField()
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
    slug = models.SlugField()
    tags = TaggableManager(verbose_name="Taqlar")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yaradılma tarixi")

    def __str__(self):
        
        return self.title
    
    class Meta:
        verbose_name = "Bloq"
        verbose_name_plural = "Bloqlar"

class Comments(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ad")
    email = models.CharField(max_length=100,verbose_name="Elektron poçt")
    message = models.TextField(verbose_name="Mesaj")
    post = models.ForeignKey(BlogModel,on_delete=CASCADE,verbose_name='Məqalə')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Göndərilyi tarix")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Şərh"
        verbose_name_plural = "Şərhlər"

class ReplyComments(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ad")
    email = models.CharField(max_length=100,verbose_name="Elektron poçt")
    message = models.TextField(verbose_name="Mesaj")
    comment = models.ForeignKey(Comments,on_delete=CASCADE)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Göndərilyi tarix")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Şərh cavabı"
        verbose_name_plural = "Şərh cavabları"