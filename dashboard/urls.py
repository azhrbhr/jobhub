from django.urls import path
from dashboard.views import CompanyListView, JobListView, JobApplicationsView, MarkAsViewedView, ChangeStatusView

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company_list'),
    path('job/<int:pk>/applications/',
         JobApplicationsView.as_view(), name='job_applications'),
    path('job/<int:job_id>/applications/<int:application_id>/change_status/',
         ChangeStatusView.as_view(), name='change_status'),
    path('job/<int:job_id>/applications/<int:application_id>/mark_as_viewed/',
         MarkAsViewedView.as_view(), name='mark_as_viewed'),
    path('', JobListView.as_view(), name='dashboard'),
]
