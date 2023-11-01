from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import FileUploadForm

#################################
from rest_framework import viewsets
from rest_framework.response import Response
from .models import UploadedFile
from .serializers import UploadedFileSerializer

class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

    # Define a custom action to count results based on filters
    def count_results(self, request):
        filters = request.query_params  # Get query parameters from the request
        queryset = UploadedFile.objects.filter(**filters)  # Apply filters to the queryset
        count = queryset.count()  # Count the results
        return render(request,'api.html',{'count':count})
        #return Response({'count': count})


######################################
def process_uploaded_file(uploaded_file):
    with uploaded_file.file.open('rb') as file_stream:
        # Process the file stream in chunks
        for chunk in file_stream.chunks():
            # Process each chunk (you can save to disk or perform other actions here)
            pass  # Replace with your processing logic

def file_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'file_list.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()  # Save the file to the database
            process_uploaded_file(uploaded_file.file)  # Process the uploaded file's content
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})
