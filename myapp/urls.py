from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('edu/', include('edu.urls')),
    path('api/', include('edu.api_urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
