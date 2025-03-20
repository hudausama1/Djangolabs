from rest_framework import serializers
from trainee.models import Trainee  # Import the Trainee model

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'  # Include all fields from the Trainee model