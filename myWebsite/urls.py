from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    # path('',),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
