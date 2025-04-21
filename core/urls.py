
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from core import views

urlpatterns = [
    path('base/', include('base.urls')),
    path('umum/', include('umum.urls')),
    path('', include('home.urls')),
    path("keepalive/", views.keepalive, name="keepalive"),
    path('admin/auth/group/', RedirectView.as_view(url='/umum/groups/', permanent=False)),
    path("admin/", admin.site.urls),
    path("", include('admin_berry.urls'))
]
