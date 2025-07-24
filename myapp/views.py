from django.urls import path
from django.shortcuts import render,redirect
from .forms import ContactForm # type: ignore



# Create your views here.

# thisis the home page view function
def home_view(request):
    return render(request,'myapp/home.html') 


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
# define the contact_success view function
def contact_success(request):
    return render(request,'myapp/contact_success.html')
