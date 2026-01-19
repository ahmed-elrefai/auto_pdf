import csv
import os
from django.conf import settings
try:
    from weasyprint import HTML
except OSError:
    HTML = None
    print("WARNING: WeasyPrint could not be loaded. PDF generation will fail. Please install GTK3 runtime.")

from jinja2 import Template
from celery import shared_task
from .models import PDFJob

@shared_task
def generate_pdfs_from_csv(job_id):
    job = PDFJob.objects.get(id=job_id)
    csv_path = job.csv_file.path
    template_path = job.template_file.path
    output_dir = os.path.join(settings.MEDIA_ROOT, 'generated_pdfs', str(job.id))
    os.makedirs(output_dir, exist_ok=True)

    with open(template_path, encoding='utf-8') as tpl_file:
        template_content = tpl_file.read()
        jinja_template = Template(template_content)

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, 1):
            context_data = {**row, 'student': row}
            filled_html = jinja_template.render(context_data)

            pdf_path = os.path.join(output_dir, f'document_{idx}.pdf')
            if HTML:
                HTML(string=filled_html).write_pdf(pdf_path)
            else:
                raise RuntimeError("WeasyPrint is not available. Cannot generate PDF.")
    
    # Mark job as completed
    job.completed = True
    job.save()
