from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from subjects.urls import chapter_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("user.urls")),
    path("api/academies/", include("academies.urls")),
    path("api/subjects/", include("subjects.urls")),
    path("api/chapters/", include((chapter_urlpatterns, "chapters"))),
    path("api/concepts/", include("concepts.urls")),
    path("api/learning/", include("learning.urls")),
    path("api/current_affairs/", include("current_affairs.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
