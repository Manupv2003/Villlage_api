from django.contrib import admin
from .models import Job, Worker

class WorkerInline(admin.TabularInline):  # Lets you add workers directly inside the job page
    model = Worker
    extra = 1

class JobAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [WorkerInline]

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'contact_number')
    search_fields = ('name', 'contact_number')

admin.site.register(Job, JobAdmin)
#admin.site.register(Worker, WorkerAdmin)
