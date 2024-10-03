from django.contrib import admin
from django.urls import path, include
from SkillXSecond.views import CustomAuthToken
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="SkillXchange API",
        default_version='v1',
        description="API for managing courses, tutors, students, and feedback.",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@skillxchange.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('SkillXSecond.urls')),
    path('api/login/', CustomAuthToken.as_view(), name='login'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger<format>.json|yaml', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
