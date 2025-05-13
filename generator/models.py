from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class PDFJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    csv_file = models.FileField(upload_to="csv_uploads/")
    template_file = models.FileField(upload_to="templates/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    @property
    def status(self):
        return "Completed" if self.completed else "Pending"