from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):     
    queryset = Product.objects.all()  #notes:6
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "perform create is used to customise the create method, as we can see, if the content is not provided, it will be set to this default value."
        serializer.save(content=content)
            

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()  #notes:3,4,5
    serializer_class = ProductSerializer 
    # lookup_field = "pk"  this is the default field
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

    def perform_update(self, serializer): #for more custom things
        instance = serializer.save()
        # if instance.price < 10000:
        #     instance.price = 99999
        #     instance.save()
        if not instance.content:
            instance.content = "perform update is used to customise the update method, as we can see, if the content is not provided, it will be set to this default value."
            instance.save()
            
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
