from django.urls import path

from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('openapi', get_schema_view(
        title="Cargoroo API",
        description="API for cargoroo",
        version="1.0.0"
    ), name='openapi-schema'),
]
