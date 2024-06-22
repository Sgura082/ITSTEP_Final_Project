from django import forms
from .models import Visitor


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['visitor_name','visitor_last_name','visitor_ID','visitor_mobiluri']

        widgets = {
            'visitor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your Name'}),
            'visitor_last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your Lastname'}),
            'visitor_ID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your ID Number (11 char)'}),
            'visitor_mobiluri': forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                'Please enter your mobile phone number'})

        }
