from rest_framework import serializers
from .models import Course  # Import the Course model

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # Primary key
    name = serializers.CharField(max_length=50)

    @classmethod
    def translate_all_courses_to_json(cls):
        courses = Course.objects.all()
        courses_serialized = CourseSerializer(courses, many=True)
        return courses_serialized.data

    @classmethod
    def get_course_by_id(cls, id):
        return CourseSerializer(Course.objects.get(id=id))

    def create(self, validated_data):
        return Course.objects.create(name=validated_data['name'])

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance