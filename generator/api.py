from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import PDFJob
from .serializers import PDFJobSerializer
from .tasks import generate_pdfs_from_csv

class PDFJobViewSet(viewsets.ModelViewSet):
    serializer_class = PDFJobSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Return all jobs for now to simplify debugging/demo
        return PDFJob.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        # We need a user, picking the first one or None if allowed
        # For now, just save without user if the model allows, or query the first user
        from django.contrib.auth import get_user_model
        User = get_user_model()
        # Fallback to the first user for demo purposes if anonymous
        user = self.request.user if self.request.user.is_authenticated else User.objects.first()
        
        job = serializer.save(user=user)
        # Trigger async task
        generate_pdfs_from_csv.delay(job.id)
