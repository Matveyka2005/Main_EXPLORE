from django.urls import path, include


api_users_urlpatterns = [
    path("api/api-auth/", include("rest_framework.urls"))
]