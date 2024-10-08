from django.urls import path
from .views import ProtectedView, PublicView

urlpatterns = [
    path('public/', PublicView.as_view(),
         name='public-endpoint'),  # Public access
    path('protected/', ProtectedView.as_view(),
         name='protected-endpoint'),  # Requires API key
]
