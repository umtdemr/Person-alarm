from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.views import (
    deneme_view, 
    upload_file_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', deneme_view),
    path('upload-img/', upload_file_view),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
