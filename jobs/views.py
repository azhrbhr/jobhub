from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from jobs.models import Job
from django.views.generic import ListView, DetailView


class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    ordering = ['-posted_at']


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    template_name = 'jobs/job_form.html'
    fields = ['title', 'company', 'description', 'location']

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('job-list')
