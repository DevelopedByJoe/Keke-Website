
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
]  


# For Admin Page Personalisation
admin.site.site_header = "KeKe - Marhaba Admin"
admin.site.site_title = "KeKe Admin Portal"
admin.site.index_title = "Welcome To KeKe - Marhaba"


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    