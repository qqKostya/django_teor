from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path("riddles/", include("riddles.urls")),
    path("admin/", admin.site.urls),
]
