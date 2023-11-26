from django.shortcuts import render
from django.views.generic import ListView
from jobs.models import Company, Job
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from applications.models import JobApplication
from django.urls import reverse


class CompanyListView(ListView):
    model = Company
    template_name = 'dashboard/company_list.html'
    context_object_name = 'companies'


class JobListView(ListView):
    model = Job
    template_name = 'dashboard/job_list.html'
    context_object_name = 'jobs'


class JobApplicationsView(View):
    template_name = 'dashboard/job_applications.html'

    def get(self, request, pk):
        job = get_object_or_404(Job, id=pk)
        applications = job.jobapplication_set.all()
        context = {'job': job, 'applications': applications}
        return render(request, self.template_name, context)


class ChangeStatusView(View):
    def get(self, request, job_id, application_id):
        application = get_object_or_404(JobApplication, id=application_id)

        # Toggle between 'Accepted' and 'Rejected'
        if application.status == 'Accepted':
            application.status = 'Rejected'
        else:
            application.status = 'Accepted'

        application.save()
        return redirect(reverse('job_applications', args=[job_id]))


class MarkAsViewedView(View):
    def get(self, request, job_id, application_id):
        application = get_object_or_404(JobApplication, id=application_id)
        application.mark_as_viewed = True
        application.save()
        return redirect(reverse('job_applications', args=[job_id]))
