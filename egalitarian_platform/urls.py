from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('courses/', include('courses.urls')),
    path('events/', include('events.urls')),
    path('accounts/', include('accounts.urls')),
    path('exams/', include('exams.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
