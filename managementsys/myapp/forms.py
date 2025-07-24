from django import forms

class ContactForm(forms.Form):
    name =forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=500)
    
    def send_email(self):
        # Logic to send email
        print(f"Sending email to {self.cleaned_data['email']} with message: {self.cleaned_data['message']}")
