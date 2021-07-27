from .models import webUsers
from django import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model = webUsers
        fields = '__all__'
        labels = {
            'username': 'USERNAME',
            'email_id': 'EMAIL ID'
        }
        widgets = {
            'email_id': forms.EmailInput()
        }