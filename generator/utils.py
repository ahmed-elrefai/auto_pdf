import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
from django.conf import settings

def generate_pdfs_from_csv(job):
    csv_path = job.csv_file.path
    output_dir = os.path.join(settings.MEDIA_ROOT, 'generated_pdfs', str(job.id))
    os.makedirs(output_dir, exist_ok=True)

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, 1):
            pdf_path = os.path.join(output_dir, f'document_{idx}.pdf')
            c = canvas.Canvas(pdf_path, pagesize=A4)
            width, height = A4
            y = height - 100

            for key, value in row.items():
                c.drawString(100, y, f"{key}: {value}")
                y -= 20

            c.save()
