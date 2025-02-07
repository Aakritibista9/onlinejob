from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from apps.job.models import Job
from apps.userprofile.models import Userprofile

# View to display the front page with a list of active jobs
def frontpage(request):
	# Retrieve active jobs from the database, ordered by creation date
	jobs = Job.objects.filter(status=Job.ACTIVE).order_by('-created_at')

	# Render the frontpage template with the list of jobs
	return render(request, 'core/frontpage.html', {'jobs': jobs})

# Create your views here.
# def frontpage(request):
# return render(request, 'core/frontpage.html')

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()

			account_type = request.POST.get('account_type', 'jobseeker')

			if account_type == 'employer':
				userprofile = Userprofile.objects.create(user=user, is_employer=True)
				user.userprofile.save()
			else:
				userprofile = Userprofile.objects.create(user=user)
				userprofile.save()

			login(request, user)

			return redirect('dashboard')
	else:
		form = UserCreationForm()
	return render(request, 'core/signup.html' , {'form': form})


