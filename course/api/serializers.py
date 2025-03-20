from rest_framework import serializers
from ..models import Course  # Import the Course model

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'  # Include all fields from the Course model