from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api import PDFJobViewSet

router = DefaultRouter()
router.register(r'jobs', PDFJobViewSet, basename='api-jobs')

urlpatterns = [
    path('upload-job/', views.upload_pdf_job, name='upload_pdf_job'),
    path('list-jobs/', views.job_list, name='job_list'),
    path('api/', include(router.urls)),
]
