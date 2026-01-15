from django import forms
from . models import MaintenanceRequest

class UpdateMaintanenceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = [
            'title',
            'tenant',
            'status',
            'admin_notes'
        ]
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Water leakage in kitchen'
            }),
            'tenant': forms.Select(attrs={
                'class': 'form-select',
                'readonly': 'readonly'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'admin_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add notes or remarks...'
            })
        }