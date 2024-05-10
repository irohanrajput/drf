from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets, mixins

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> queryset
    get -> retrieve -> product instance
    post -> create -> new product instance
    put -> update -> update 
    pathc -> update -> partial update
    delete -> destroy -> delete
    '''
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    
    
class ProductGenericViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin
                            ):
    
    '''
    get -> list -> queryset
    get -> retrieve -> product instance
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    
    
product_list_view = ProductViewSet.as_view({"get": "list"})