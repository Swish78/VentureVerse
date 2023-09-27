from django import forms
from .models import JobListing, LOCATION_CHOICES, SKILL_CHOICES

class JobForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['title', 'description', 'company', 'location', 'skills']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'skills': forms.CheckboxSelectMultiple(),
        }
