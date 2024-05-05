from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()  #notes:3,4,5
    serializer_class = ProductSerializer 
    # lookup_field = 'pk'