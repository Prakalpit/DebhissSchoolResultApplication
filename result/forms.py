from .models import Result
from django import forms

class UploadResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'

