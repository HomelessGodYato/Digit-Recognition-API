from django.db import models


class Image(models.Model):
    filename = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.prediction
    
class Prediction(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='prediction')
    prediction = models.IntegerField(blank=False, default=0, null=False)
    confidence = models.FloatField(blank=False, default=0.0, null=False)

    def __str__(self):
        return self.prediction