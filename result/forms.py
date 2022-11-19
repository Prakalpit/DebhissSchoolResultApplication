from .models import Result
from django import forms

class UploadResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'grade_class': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.Textarea(attrs={'class': 'form-control'}),
            'remarks': forms.TextInput(attrs={'class': 'form-control'}),
        }

