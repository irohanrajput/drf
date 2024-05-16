from rest_framework import serializers
from .models import Product 
 
 
def validate_title(self, value):
    qs = Product.objects.filter(title__iexact=value)
    if qs:
        raise serializers.ValidationError("This title already exists")
    return value