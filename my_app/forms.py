from django import forms
from .models import MyModel


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name', 'surname', 'dob']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
