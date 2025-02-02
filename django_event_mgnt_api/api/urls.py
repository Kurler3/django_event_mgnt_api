
from django.urls import path, include

urlpatterns = [
    path('v1/', include('api.v1.urls')),  # Routes requests to v1
    path('v2/', include('api.v2.urls')),  # Routes requests to v2
]
