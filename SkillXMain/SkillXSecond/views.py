from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, viewsets, permissions
from django.contrib.auth import authenticate
from .models import Course, CourseRate
from .serializers import CourseSerializer, CourseRateSerializer



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.request.user.is_staff:  # Admin has full access
            return [permissions.IsAdminUser()]
        elif hasattr(self.request.user, 'is_tutor') and self.request.user.is_tutor:  
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticatedOrReadOnly()]  

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  

    def get_queryset(self):
        if self.request.user.is_staff:  # Admin sees all courses
            return Course.objects.all()
        elif hasattr(self.request.user, 'is_tutor') and self.request.user.is_tutor:  
            return Course.objects.filter(owner=self.request.user)
        return Course.objects.filter(is_active=True)  



class CourseRateViewSet(viewsets.ModelViewSet):
    queryset = CourseRate.objects.all()
    serializer_class = CourseRateSerializer

    def get_permissions(self):
        if self.request.user.is_staff or hasattr(self.request.user, 'is_student') and self.request.user.is_student:
            return [permissions.IsAuthenticated()] 
        return [permissions.IsAuthenticatedOrReadOnly()]  



class CustomAuthToken(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

