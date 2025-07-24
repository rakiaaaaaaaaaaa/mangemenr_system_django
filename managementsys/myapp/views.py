from django.urls import path
from django.shortcuts import render,redirect
from .form import ContactForm # type: ignore
from .views import index


# Create your views here.

# thisis the home page view function
def home_view(request):
    return render(request,'myapp/index.html') 


# this is the contact page view function
def contact_view(request):
    if request.method =='POST':
        form =ContactForm(request.POST)
        if form.isValid():
            form.send_email()
            return redirect('contact success')
    else:
        form = ContactForm()
    context = { 'form': form}    
    return render(request, 'myapp/contact.html', context)    
