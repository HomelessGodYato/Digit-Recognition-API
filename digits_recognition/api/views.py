from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .apps import ApiConfig
from deeplearning.prediction import predict
from .serializers import ImageSerializer
from .models import Image, Prediction


class PredictionViewSet(APIView):
    @csrf_exempt
    def post(self, request):
        model = ApiConfig.model
        try:
            serializer = predict(request, model)
            return JsonResponse(data = serializer.data, status=200)
        except KeyError:
            return JsonResponse({'Bad request': 'Image not included in request'}, status=400)
 

    @csrf_exempt
    def get(self, request):
        try:
            image_id = request.GET.get('id')
            if image_id is not None:
                try:
                    image = Image.objects.get(id=image_id)
                except Image.DoesNotExist:
                    return JsonResponse({'message': 'Image not found'}, status=404)
                
                serializer = ImageSerializer(image)
                return JsonResponse(data = serializer.data, status=200)

            images = Image.objects.all()
            print("HERE")
            serializer = ImageSerializer(images, many=True)
            return JsonResponse(data = serializer.data, status=200, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse({'message': 'Internal server error'}, status=500)

    
    @csrf_exempt
    def delete(self, request):
        try:
            image_id = int(request.GET.get('id'))
            try:
                image = Image.objects.get(id=image_id)
                image.delete()
                return JsonResponse({'message': 'Image deleted'}, status=202)
            except Image.DoesNotExist:
                return JsonResponse({'message': 'Image not found'}, status=204)
        except Exception as e:
            return JsonResponse({'message': f'{e}'}, status=500)
        
        except:
            return JsonResponse({'message': 'Bad Request'}, status=400)
