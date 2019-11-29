from django import forms

from .models import Contact



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('fullName', 'phone', 'email', 'message')
        widgets = {
            'fullName': forms.TextInput(attrs={'class': 'input'}),
            'phone': ,
            'email': forms.EmailField(attrs={'class': 'input'}),
            'message': forms.Textarea(attrs={'class': 'textarea'}),
        }