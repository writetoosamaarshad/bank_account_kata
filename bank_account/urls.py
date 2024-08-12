from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Bank Account API",
        default_version='v1',
        description="API documentation for the Bank Account Kata challenge",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Include URLs from the accounts app
    path('api/', include('accounts.urls')),

    # Swagger UI for API documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
