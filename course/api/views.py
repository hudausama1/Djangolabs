from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Course
from .serializers import CourseSerializer

@api_view(['PUT'])
def update_course(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Course updated successfully",
            "data": serializer.data,
        }, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)