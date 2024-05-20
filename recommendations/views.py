from django.shortcuts import render
from django.http import JsonResponse

def get_job_recommendations(request, user_id):
    # Retrieve the similarity matrix from the CSV file
    job_similarity_df = pd.read_csv('job_similarity_matrix.csv', index_col=0)

    # Get jobs the user has interacted with
    user_interactions = JobInteraction.objects.filter(user=user_id)
    user_jobs = [interaction.job_id for interaction in user_interactions]

    # Find jobs similar to the ones the user has interacted with
    similar_jobs = []
    for job_id in user_jobs:
        similar_jobs.extend(job_similarity_df[job_id].sort_values(ascending=False).index)

    # Remove already interacted jobs
    recommended_jobs = [job for job in similar_jobs if job != job_id and job not in user_jobs][:5]

    return JsonResponse({'recommended_jobs': recommended_jobs})


