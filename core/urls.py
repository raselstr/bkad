
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from core import views

urlpatterns = [
    path('search/', include('dokumen.urls')),
    path('base/', include('base.urls')),
    path('umum/', include('umum.urls')),
    path('', include('home.urls')),
    path("keepalive/", views.keepalive, name="keepalive"),
    path('admin/auth/group/', RedirectView.as_view(url='/umum/groups/', permanent=False)),
    path('send-email/', views.test_email, name='send_email'),
    path("admin/", admin.site.urls),
    path("", include('admin_berry.urls'))
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)