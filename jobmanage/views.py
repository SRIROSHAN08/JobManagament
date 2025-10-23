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

       
        if search and JobDetails.objects.filter(company_name__iexact=search).exists():
            queryset = queryset.filter(company_name__iexact=search)

        
        elif location and JobDetails.objects.filter(location__iexact=location).exists():
            queryset = queryset.filter(location__iexact=location)

        
        else:
            q_list = []

            if search:
                q_list.append(Q(title__icontains=search) | Q(company_name__icontains=search))
            if location:
                q_list.append(Q(location__iexact=location))  
            if job_type:
                q_list.append(Q(job_type__iexact=job_type))  
            if salary:
                try:
                    q_list.append(Q(salary_range__gte=int(salary)))
                except ValueError:
                    pass  

            
            if q_list:
                queryset = queryset.filter(reduce(lambda x, y: x & y, q_list))
            elif not any([search, location, job_type, salary]):
                queryset = JobDetails.objects.all()
            
        print(salary)
        
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
        
        return render(request,'home.html',context)
