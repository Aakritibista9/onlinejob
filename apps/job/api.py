import json

from django.db.models import Q
from django.http import JsonResponse

from .models import Job

def api_search(request):
    # Initialize an empty list to store job details
    jobslist = []
    data = json.loads(request.body)
    query = data['query']
    company_size = data['company_size']

    # Use the Django ORM to filter jobs based on the search query
    # The Q object is used for making complex queries with OR conditions
    jobs = Job.objects.filter(status=Job.ACTIVE).filter(Q(title__icontains=query) | Q(short_description__icontains=query) | Q(long_description__icontains=query) | Q(company_name__icontains=query) | Q(company_place__icontains=query))

    # If a company size is specified, further filter jobs by company size
    if company_size:
        jobs = jobs.filter(company_size=company_size)

    # Iterate through the filtered jobs and create a list of dictionaries
    # containing job details    
    for job in jobs:
        obj = {
            'id': job.id,
            'title': job.title,
            'company_name': job.company_name,
            'url': '/jobs/%s/' % job.id
        }
        jobslist.append(obj)
    # Return a JSON response containing the list of jobs
    return JsonResponse({'jobs': jobslist})



