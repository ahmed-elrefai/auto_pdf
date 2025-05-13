from django import forms
from .models import PDFJob


class PDFJobForm(forms.ModelForm):
    class Meta:
        model = PDFJob
        fields = ['csv_file', 'template_file']