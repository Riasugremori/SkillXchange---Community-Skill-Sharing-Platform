from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ADMINISTRATOR = 'administrator'
    TUTOR = 'tutor'
    STUDENT = 'student'

    ROLE_CHOICES = [
        (ADMINISTRATOR, 'Administrator'),
        (TUTOR, 'Tutor'),
        (STUDENT, 'Student'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT)  


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  
        blank=True
    )





class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tutor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.title



class CourseRate(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    rating = models.PositiveIntegerField()  
    feedback = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating for {self.course.title} by {self.student.username}"