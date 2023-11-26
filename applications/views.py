# You need to create a form for JobApplication
from .forms import JobApplicationForm
from .models import JobApplication
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from applications.models import JobApplication
from jobs.models import Job


class MyJobsListView(ListView):
    model = JobApplication
    template_name = 'applications/my_jobs.html'
    context_object_name = 'job_applications'
    ordering = ['-applied_at']

    def get_queryset(self):
        return JobApplication.objects.filter(applicant=self.request.user)


class JobApplicationListView(ListView):
    model = JobApplication
    template_name = 'applications/job_application_list.html'
    context_object_name = 'applications'


class JobApplicationDetailView(DetailView):
    model = JobApplication
    template_name = 'applications/job_application_detail.html'
    context_object_name = 'application'


class JobApplicationCreateView(CreateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'applications/job_application_form.html'
    success_url = '/success/'  # Replace with the desired success URL

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        form.instance.job = get_object_or_404(Job, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = get_object_or_404(Job, pk=self.kwargs['pk'])
        return context


class JobApplicationUpdateView(UpdateView):
    model = JobApplication
    template_name = 'applications/job_application_form.html'
    fields = ['job', 'applicant', 'cover_letter',
              'status']  # Add or remove fields as needed
    success_url = reverse_lazy('job_application_list')


class JobApplicationDeleteView(DeleteView):
    model = JobApplication
    template_name = 'applications/job_application_confirm_delete.html'
    success_url = reverse_lazy('job_application_list')
