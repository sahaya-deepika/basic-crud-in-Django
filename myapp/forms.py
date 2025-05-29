from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'age', 'symptoms', 'gender', 'contact_number']
