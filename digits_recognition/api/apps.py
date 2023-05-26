from django.apps import AppConfig
import tensorflow as tf
import os
from django.conf import settings

class ApiConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    model = tf.keras.models.load_model(settings.MODEL_PATH["model"])