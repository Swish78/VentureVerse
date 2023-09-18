from django import forms

ROLE_CHOICES = [
    ('employee', 'Employee'),
    ('employer', 'Employer'),
]

class RoleSelectionForm(forms.Form):
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        label="Select Your Role"
    )

    def clean_role(self):
        role = self.cleaned_data.get('role')
        if not role:
            raise forms.ValidationError("Please select a role.")
        return role

class EmployeeRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    experience = forms.FloatField(label="Experience")
    DOB = forms.DateField(label="Date of Birth")
    # Add more fields as needed for employee registration

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Add custom email validation if needed
        return email

class EmployerRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    company_name = forms.CharField(max_length=100, label="Company Name")
    industry = forms.CharField(max_length=100, label="Industry")
    employee_count = forms.FloatField(label="Employee Count", max_value=50)
    location_choices = [
        ('Mumbai', 'Mumbai'),
        ('Pune', 'Pune'),
        ('Bengaluru', 'Bengaluru'),
        ('Hyderabad', 'Hyderabad'),
        ('Delhi', 'Delhi'),
        ('Indore', 'Indore'),
        ('Other', 'Other'),
    ]
    location = forms.ChoiceField(choices=location_choices, label="Location")

    def clean_company_name(self):
        company_name = self.cleaned_data.get('company_name')
        # Add custom company name validation if needed
        return company_name
