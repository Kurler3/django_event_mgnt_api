from django.urls import path
from .views.example import ExampleV2View

urlpatterns = [
    path('example/', ExampleV2View.as_view(), name='v2-example'),
]
