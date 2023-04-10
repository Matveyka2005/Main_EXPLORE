from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    url_debug = [
        path('__debug__/', include('debug_toolbar.urls')),
                 ]
    urlpatterns += url_debug
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

