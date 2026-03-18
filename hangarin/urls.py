from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import HangarinLoginView, dashboard, home

urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("login/", HangarinLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
