from django.contrib import admin
from jobs.models import Company, Job


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'posted_at', 'updated_at']


admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)
