from django.db import models

# Create your models here.

STATUS = (
    ("false","Baxılmayıb"),
    ("true","Baxılıb"),
)

class ContactModel(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ad")
    email = models.CharField(max_length=100, verbose_name="Email")
    subject = models.CharField(max_length=100,verbose_name="Mövzu")
    message = models.TextField(verbose_name="Mesaj")
    status = models.CharField(max_length=100,choices=STATUS,default="false")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Göndərilmə tarixi")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Əlaqə"
        verbose_name_plural = "Əlaqə"