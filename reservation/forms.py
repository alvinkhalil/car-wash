from django import forms
from django.db.models.fields import TextField
from django.forms import widgets
from reservation.models import ReservationModel
class PriceForm(forms.ModelForm):
    class Meta:
        model = ReservationModel

        fields = ["name","email","phone","plan","message"]
        widgets ={
            "name":         widgets.Input(attrs={'class':'form-control', 'placeholder':"Ad", 'required':'required'}),
            'email':        widgets.EmailInput(attrs={'class':'form-control', 'placeholder':"Email", 'required':'required'}),
            "phone":         widgets.TextInput(attrs={'class':'form-control', 'placeholder':"Əlaqə nömrəsi", 'required':'required'}),
            "message":         widgets.Textarea(attrs={'class':'form-control', 'placeholder':"Əlavə mesaj", 'required':'required'}),



        }



