from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# Job model represents a job posting in the system
class Job(models.Model):
	# ForeignKey to User model, represents the user who created the job
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	SIZE_1_9 = 'size_1-9'
	SIZE_10_49 = 'size_10-49'
	SIZE_50_99 = 'size_50-99'
	SIZE_100 = 'size_100'

	CHOICES_SIZE = (

		(SIZE_1_9, '1-9'),
		(SIZE_10_49, '10-49'),
		(SIZE_50_99, '50-99'),
		(SIZE_100, '100+'),

		)

	ACTIVE = 'active'
	EMPLOYED = 'employed'
	ARCHIVED = 'archived'

	CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (EMPLOYED, 'Employed'),
        (ARCHIVED, 'Archived'),


        )

	title = models.CharField(max_length=255)
	short_description = models.TextField()
	long_description = models.TextField(blank=True, null=True)
	company_name = models.CharField(max_length=255)
	company_address = models.CharField(max_length=255, blank=True, null=True)
	company_zipcode = models.CharField(max_length=255, blank=True, null=True)
	company_place = models.CharField(max_length=255, blank=True, null=True)
	company_country = models.CharField(max_length=255, blank=True, null=True)
	company_size = models.CharField(max_length=20, choices=CHOICES_SIZE, default=SIZE_1_9)

	created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	changed_at = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=ACTIVE)

	def __str__(self):
		return self.title

# Application model represents a job application in the system
class Application(models.Model):
	# ForeignKey to Job model, represents the job to which the application belongs
	job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)

	# Fields for the Application model
	content = models.TextField()
	experience = models.TextField()
	created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	# Comment explaining the purpose of the Application model
    # Represents the details of job applications submitted by users for specific jobs



