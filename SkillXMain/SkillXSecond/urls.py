from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, CourseRateViewSet


router = DefaultRouter()


router.register(r'Course', CourseViewSet)
router.register(r'CourseRate', CourseRateViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
