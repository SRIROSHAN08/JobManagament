from django import forms
from .models import JobDetails

class JobDetails_Form(forms.ModelForm):
    LOCATION_CHOICES = [
        ("", "Choose Preferred Location"),
        ("Chennai", "Chennai"),
        ("Bangalore", "Bangalore"),
        ("Hyderabad", "Hyderabad"),
        ("Mumbai", "Mumbai"),
        ("Remote", "Remote"),
    ]
    JOB_TYPE_CHOICES = [
        ("", "Choose Job Type"),
        ("full time", "FullTime"),
        ("part time", "PartTime"),
        ("contract", "Contract"),
        ("internship", "Internship"),
    ]
    location = forms.ChoiceField(choices=LOCATION_CHOICES, widget=forms.Select(attrs={'class': 'modal-select'}))
    job_type = forms.ChoiceField(choices=JOB_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'modal-select'}))
    
    class Meta:
        model = JobDetails
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Job Title'}),
            'company_name': forms.TextInput(attrs={'placeholder': 'Amazon, Microsoft, Swiggy'}),
            'salary_range': forms.TextInput(attrs={'placeholder': 'e.g. ₹12,00,000', 'class': 'modal-salary'}),
            'application_deadline': forms.DateInput(attrs={'type': 'date', 'class': 'modal-date'}),
            'job_description': forms.Textarea(attrs={'placeholder': 'Description', 'rows': 3}),
        }
