from django.contrib import admin
from applications.models import JobApplication


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job', 'status', 'applied_at', 'updated_at']
    list_filter = ['status', 'job']
    search_fields = ['applicant__username', 'job__title']


admin.site.register(JobApplication, JobApplicationAdmin)
