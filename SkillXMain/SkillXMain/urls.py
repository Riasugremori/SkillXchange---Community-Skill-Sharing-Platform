from django.contrib import admin
from django.urls import path, include
from SkillXSecond.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('SkillXSecond.urls')),
    path('api/login/', CustomAuthToken.as_view(), name='login')
]
