from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view

from api.urls import api

urlpatterns = [
    path('api/', include(api.urls)),
    path('openapi-schema/', get_schema_view(
        title="Cargoroo API",
        description="API for cargoroo",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
