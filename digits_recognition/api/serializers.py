from rest_framework.serializers import ModelSerializer
from .models import Image, Prediction

class PredictionSerializer(ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['prediction', 'confidence']


class ImageSerializer(ModelSerializer):
    prediction = PredictionSerializer(many=True, read_only=True)
    class Meta:
        model = Image
        fields = ['filename', 'prediction']
        