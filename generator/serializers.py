from rest_framework import serializers
from .models import PDFJob
from django.conf import settings
import os

class PDFJobSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    pdf_files = serializers.SerializerMethodField()
    
    class Meta:
        model = PDFJob
        fields = ['id', 'user', 'csv_file', 'template_file', 'created_at', 'completed', 'status', 'pdf_files']
        read_only_fields = ['user', 'completed', 'created_at']

    def get_pdf_files(self, obj):
        files = []
        output_dir = os.path.join(settings.MEDIA_ROOT, 'generated_pdfs', str(obj.id))
        if os.path.exists(output_dir):
            for filename in os.listdir(output_dir):
                file_url = f"{settings.MEDIA_URL}generated_pdfs/{obj.id}/{filename}"
                # Construct absolute URL if request is available
                request = self.context.get('request')
                if request is not None:
                    file_url = request.build_absolute_uri(file_url)
                files.append(file_url)
        return files
