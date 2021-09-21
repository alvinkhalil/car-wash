from contact.models import ContactModel
from django.shortcuts import redirect, render
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        contact = ContactModel(name = name, email = email, subject = subject, message = message)
        contact.save()
        messages.success(request,"Mesajınız üçün təşəkkür edirik.")

    return render(request,"pages/contact.html")