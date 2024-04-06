# forms.py
from django import forms
from .models import Hospital, Doctor

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'location']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialty', 'hospital']
