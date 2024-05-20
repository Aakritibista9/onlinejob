from django.urls import path
from . import views

urlpatterns = [
    path('get_recommendations/<int:user_id>/', views.get_job_recommendations, name='get_recommendations'),
]