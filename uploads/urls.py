from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from uploads.views import upload_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_image),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
