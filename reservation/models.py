from django.db import models

# Create your models here.

STATUS = (
    ("True","Qəbul edilib"),
    ("False","Gözləmədə"),
)

class ReservationModel(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ad Soyad")
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100,verbose_name="Telefon")
    message = models.TextField(verbose_name="Mesaj")
    status = models.CharField(choices=STATUS, default="False",max_length=100,verbose_name="Status")

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rezerv"
        verbose_name_plural = "Rezervlər"
