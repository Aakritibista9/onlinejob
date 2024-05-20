# recommendations/utils.py
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def calculate_job_similarity():
    # Fetch job interactions data
    interactions = JobInteraction.objects.all()
    
    # Create a user-job interaction matrix
    user_job_matrix = pd.crosstab(interactions['user'], interactions['job'], values=interactions['interaction_type'], aggfunc='count').fillna(0)
    
    # Calculate job-job similarity using cosine similarity
    job_similarity = cosine_similarity(user_job_matrix.T)
    
    # Store the similarity matrix for later use
    job_similarity_df = pd.DataFrame(job_similarity, index=user_job_matrix.columns, columns=user_job_matrix.columns)
    job_similarity_df.to_csv('job_similarity_matrix.csv')