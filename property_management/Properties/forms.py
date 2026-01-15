from django import forms
from . models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'name',
            'address',
            'property_type',
            'rent_amount',
            'description',
            'image',
            'is_occupied',
            'tenant',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter property name'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Enter address'
            }),
            'property_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'rent_amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '₹'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter description'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_occupied': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'occupied'
            }),
            'tenant': forms.Select(attrs={
                'class': 'form-select'
            }),
        }