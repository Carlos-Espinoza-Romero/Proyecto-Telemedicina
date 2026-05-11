from django.urls import path, include

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('medical/', include('medical.urls')),
]
