from django import forms

class RoleSelectionForm(forms.Form):
    role_choices = [
        ('employee', 'Employee'),
        ('employer', 'Employer'),
    ]
    role = forms.ChoiceField(
        choices=role_choices,
        widget=forms.RadioSelect,
        required=True,
        label="Select Your Role"
    )

    def clean_role(self):
        role = self.cleaned_data.get('role')
        if not role:
            raise forms.ValidationError("Please select a role.")
        return role
