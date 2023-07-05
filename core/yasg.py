
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Slug_product_API",
        default_version="vi",
        description="API documention for Slug Product",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(
            name="shekhnaz",
            email="adulzhanova2021@icloud.com",
            url="https://github.com/mooonalikaya",
        ),
        license=openapi.License(
            name="BSD license"
        ),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-documentation'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-documentation'),
]