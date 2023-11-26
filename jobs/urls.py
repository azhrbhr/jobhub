from django.urls import path
from jobs.views import JobCreateView, JobListView, JobDetailView
from applications.views import JobApplicationCreateView

urlpatterns = [
    path('create/', JobCreateView.as_view(), name='job_create'),
    path('list/', JobListView.as_view(), name='job_list'),
    path('<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('<int:pk>/apply/', JobApplicationCreateView.as_view(), name='apply_job'),
]
