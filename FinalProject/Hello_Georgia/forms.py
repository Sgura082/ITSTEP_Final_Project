from django import forms
from .models import Visitor
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
class VisitorForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('Home')

        self.helper.add_input(Submit('submit','Submit'))

    class Meta:
        model = Visitor
        fields = ['visitor_name','visitor_last_name','visitor_ID','visitor_mobiluri']

        widgets = {
            'visitor_name': forms.TextInput(attrs={'height':200,'hx-get':reverse_lazy('Home'), 'hx-trigger': 'keyup','height':'200px' ,'class': 'form-control', 'placeholder': 'Please enter your Name'}),
            'visitor_last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your Lastname'}),
            'visitor_ID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your ID Number (11 char)'}),
            'visitor_mobiluri': forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                'Please enter your mobile phone number'})

        }
