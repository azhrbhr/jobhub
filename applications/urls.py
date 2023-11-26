from django.urls import path
from applications.views import MyJobsListView, JobApplicationListView, JobApplicationDetailView, JobApplicationCreateView, JobApplicationUpdateView, JobApplicationDeleteView

urlpatterns = [
    path('myjobs/', MyJobsListView.as_view(), name='my_jobs'),
    path('', JobApplicationListView.as_view(), name='job_application_list'),
    path('<int:pk>/', JobApplicationDetailView.as_view(),
         name='job_application_detail'),
    path('create/', JobApplicationCreateView.as_view(),
         name='job_application_create'),
    path('<int:pk>/edit/', JobApplicationUpdateView.as_view(),
         name='job_application_edit'),
    path('<int:pk>/delete/', JobApplicationDeleteView.as_view(),
         name='job_application_delete'),
]
