1. serializers
>>While defining a serializer class, we essentially define a blueprint for how to serialize and deserialize instances of that particular model.


2. When we want to serialize a specific instance of that model, we create an instance of Serializer and pass the model instance as the instance parameter for serializing and deserializing.



3. Retrieving the Object:

>>The queryset (Product.objects.all() in this case) is used to fetch the specific object from the database.

>>If not present, it looks for a get_queryset() method to determine the queryset dynamically. If this method is not overridden, it raises an error.

>>The queryset retrieves the specific object based on the lookup field (primary key pk by default, but can be customized using lookup_field).


4.Serializing the Object:

>>Once the object is retrieved, it is passed to the serializer class (ProductSerializer in this case) for serialization.

>>The serializer takes the Python object (in this case, a Product instance) and converts it into a JSON representation according to the fields specified in the serializer.


5. Returning the Response:

>>Finally, the serialized data is returned as an HTTP response to the client.


6. queryset in create method is not neccesarily neccesary, 

>> the createapiVIEW is still working  when we remove it, but it is for other purposes i.e. post req without using generics etc


7. authentication and permission

>> we declared the "permission_class' to be "IsAuthenticated". and now, to handle the permissions, we need to setup an authentication system. and that's where. "from rest_framework import authentication" comes in.


8. hyperlinkIdentityFields

>> The serializers.HyperlinkedIdentityField is used to represent hyperlinks to individual instances of a model.often used in conjunction with serializers.


from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    
    class Meta:
        model = Product
        fields = ['url', 'pk', 'title', 'description', 'price']
        
url is an instance of HyperlinkedIdentityField added to the serializer.