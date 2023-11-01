from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UploadedFileViewSet, upload_file, file_list  # Import your views

router = DefaultRouter()
router.register(r'uploadedfiles', UploadedFileViewSet)

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('files/', file_list, name='file_list'),
    path('api/', include(router.urls)),
    path('api/uploadedfiles/count/', UploadedFileViewSet.as_view({'get': 'count_results'}), name='count_results'),
]
