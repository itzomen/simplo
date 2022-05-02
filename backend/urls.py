from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path(
        "",
        include_docs_urls(
            title="Simplo API",
            description="API for Testing by @itzomen",
        ),
        name="simplo-docs",
    ),
    path(
        "schema/",
        get_schema_view(
            title="Simplo API", description="API for Testing by @itzomen", version="2.0.0"
        ),
        name="simplo-schema",
    ),
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/category/', include('category.urls')),
    path('api/webhook/', include('webhook.urls')),
]

# setting this to view media files from admin panel
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
