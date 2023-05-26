from api.models import Image, Prediction
from api.serializers import ImageSerializer
from image_processing import processing
import cv2
import numpy as np

def predict(request, model):
    image_object = Image.objects.create(filename=request.FILES['image'].name)

    image_file = request.FILES['image']
    image_file.seek(0)

    image_file = image_file.read()
    image_array = np.fromstring(image_file, np.uint8)
    image_array = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    classifier = model

    image_array = processing.resize_image(image_array)
    image_array = processing.convert_to_tensor(image_array)
    image_array = processing.normalize_image(image_array)

    prediction = classifier.predict(image_array)
    label = np.argmax(prediction, axis=1)
    confidence = np.max(prediction, axis=1)

    Prediction(image = image_object,
                       prediction=label, 
                       confidence=confidence).save()
    
    serializer = ImageSerializer(image_object)
    return serializer