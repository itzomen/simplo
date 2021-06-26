from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from .views import getRoutes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', getRoutes, name="routes"),
    path('api/user/', include('user.urls')),
]

# setting this to view media files from admin panel
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
