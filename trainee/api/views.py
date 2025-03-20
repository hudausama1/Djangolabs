from rest_framework import generics
from trainee.models import Trainee
from .serlizer import TraineeSerializer

class TraineeListAPIView(generics.ListAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

class TraineeCreateAPIView(generics.CreateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

class TraineeUpdateAPIView(generics.UpdateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

class TraineeDeleteAPIView(generics.DestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer