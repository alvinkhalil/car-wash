from django.db import models

# Create your models here.
STATUS = (
        ("active","Paylaşılıb"),
        ("draft","Qaralama"),
    )
class Coverimages(models.Model):



    name = models.CharField(max_length=100,verbose_name="Ad")
    title = models.CharField(max_length=100,verbose_name="Başlıq",blank=True)
    description = models.TextField(verbose_name="Məlumat")
    image = models.ImageField(upload_to = "sliders",verbose_name="Şəkil")
    status = models.CharField(choices=STATUS,max_length=100,verbose_name="Status")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        
        verbose_name = "Örtük şəkili"
        verbose_name_plural = "Örtük şəkilləri"

class Teams(models.Model):

    name = models.CharField(max_length=100,verbose_name="Ad Soyad")
    job = models.CharField(max_length=100,verbose_name="İş")
    image= models.ImageField(upload_to = "teams")
    facebook = models.CharField(max_length=1000, blank=True)
    instagram = models.CharField(max_length=1000, blank=True)
    twitter = models.CharField(max_length=1000, blank=True)
    instagram = models.CharField(max_length=1000, blank=True)
    linkedin = models.CharField(max_length=1000, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Komanda"
        verbose_name_plural = "Komandalar"

class Facts(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ad")
    servicepoints = models.IntegerField(verbose_name="Servis sayı")
    workers = models.IntegerField(verbose_name="İşçi sayı")
    clients = models.IntegerField(verbose_name="Müştəri məmuniyyəti")
    projectsompleted = models.IntegerField(verbose_name="Tamamlanmış işlər")
    status = models.CharField(choices=STATUS,max_length=100)
    updated_date =models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fakt"
        verbose_name_plural = "Faktlar"
    