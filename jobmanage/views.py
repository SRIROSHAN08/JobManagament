from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *
from django.db.models import Q
from functools import reduce

class JobView(View):
    
    def get(self, request):
        queryset = JobDetails.objects.all()

        search = request.GET.get("search", "").strip()
        location = request.GET.get("location", "").strip()
        job_type = request.GET.get("job_type", "").strip()
        salary = request.GET.get("salary", "").strip()

        filters = Q()

        # Search by title or company name
        if search:
            filters &= Q(title__icontains=search) | Q(company_name__icontains=search)

        # Exact match location
        if location:
            filters &= Q(location__iexact=location)

        # Job type filter
        if job_type:
            filters &= Q(job_type__iexact=job_type)

        # Salary filter (show jobs with salary >= selected)
        if salary:
            try:
                filters &= Q(salary_range__gte=int(salary))
            except ValueError:
                pass

        # Apply all filters if any
        if filters:
            queryset = queryset.filter(filters)

        form = JobDetails_Form()
        context = {
            'all_jobs': queryset,
            'form': form,
        }
        return render(request, 'job/home.html', context)

        
    def post(self, request):
        form = JobDetails_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
        all_jobs = JobDetails.objects.all()
        context = {
            'all_jobs':all_jobs , 'form':form,
        }
        
        return render(request,'job/home.html',context)
