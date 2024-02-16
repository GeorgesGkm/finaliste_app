from django.urls import include, path

from .views import authView, index

urlpatterns = [
    path("index", index, name='dashboard'),
    path("signup/", authView, name='authView'),
    path("accounts/", include("django.contrib.auth.urls")),
]