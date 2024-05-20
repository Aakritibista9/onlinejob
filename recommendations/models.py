from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
   

class JobInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=255)