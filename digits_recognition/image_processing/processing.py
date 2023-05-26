import cv2
import numpy as np

def resize_image(image):
    return cv2.resize(image, (28, 28))

def convert_to_tensor(image):
    return np.expand_dims(image, axis=0)

def normalize_image(image):
    return image / 255.0