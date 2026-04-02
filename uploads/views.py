from django.shortcuts import render
from .forms import UploadForm
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")

def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})
