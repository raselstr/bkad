
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('umum/', include('umum.urls')),
    path('', include('home.urls')),
    path("admin/", admin.site.urls),
    path("", include('admin_berry.urls'))
]
