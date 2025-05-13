from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PDFJobForm
from .models import PDFJob
from .utils import generate_pdfs_from_csv
from django.conf import settings
import os

@login_required
def upload_pdf_job(request):
    if request.method == 'POST':
        form = PDFJobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            
            # 🔥 Generate PDFs
            generate_pdfs_from_csv(job)

            job.completed = True
            job.save()

            return redirect('job_list')
    else:
        form = PDFJobForm()
    return render(request, 'generator/upload_job.html', {'form': form})
    
@login_required
def job_list(request):
    jobs = PDFJob.objects.filter(user=request.user)

    # Attach list of PDF paths per job
    for job in jobs:
        job.pdf_files = []
        output_dir = os.path.join(settings.MEDIA_ROOT, 'generated_pdfs', str(job.id))
        if os.path.exists(output_dir):
            for filename in os.listdir(output_dir):
                file_url = f"{settings.MEDIA_URL}generated_pdfs/{job.id}/{filename}"
                job.pdf_files.append(file_url)

    return render(request, 'generator/job_list.html', {'jobs': jobs})