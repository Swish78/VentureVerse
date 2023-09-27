from django.shortcuts import render, redirect
from .models import JobListing
from .forms import JobForm
from django.contrib.auth.decorators import login_required
from .models import JobListing

def job_listing(request):
    job_listings = JobListing.objects.all()  # Retrieve all job listings
    return render(request, 'jobs/job_listing.html', {'job_listings': job_listings})

@login_required
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job_listing = form.save(commit=False)
            job_listing.poster = request.user
            job_listing.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/job_form.html', {'form': form})
