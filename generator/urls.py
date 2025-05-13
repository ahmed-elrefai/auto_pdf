from django.urls import path
from . import views

urlpatterns = [
    path('upload-job/', views.upload_pdf_job, name='upload_pdf_job'),
    path('jobs/', views.job_list, name='job_list'),
]
