from django.db import models
from datetime import date
class JobDetails(models.Model):

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
    title = models.CharField(max_length=250,null= True, blank=True)
    company_name = models.CharField(max_length=250,null= True, blank=True)
    location = models.CharField(max_length=250,null= True,choices=LOCATION_CHOICES,blank= True)
    job_type = models.CharField(max_length=20,choices=JOB_TYPE_CHOICES,null=True) 
    salary_range = models.CharField(max_length=250,null=True,blank=True)
    job_description = models.TextField(default='Description')
    Application_deadline = models.DateField(default=date.today,null= True,blank=True)