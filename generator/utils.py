import csv
import os
from django.conf import settings
from weasyprint import HTML

def generate_pdfs_from_csv(job):
    csv_path = job.csv_file.path
    template_path = job.template_file.path  # assuming user uploads the HTML template
    output_dir = os.path.join(settings.MEDIA_ROOT, 'generated_pdfs', str(job.id))
    os.makedirs(output_dir, exist_ok=True)

    with open(template_path, encoding='utf-8') as tpl_file:
        html_template = tpl_file.read()

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, 1):
            filled_html = html_template
            for key, value in row.items():
                filled_html = filled_html.replace(f'{{{{ {key} }}}}', value)

            pdf_path = os.path.join(output_dir, f'document_{idx}.pdf')
            HTML(string=filled_html).write_pdf(pdf_path)
