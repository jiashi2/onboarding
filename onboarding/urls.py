from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.OnboardView.as_view(), name="onboard"),
    path("recv_data", views.recv_data, name="recv_data"),
    path("onboarded", views.onboarded, name="onboarded"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
