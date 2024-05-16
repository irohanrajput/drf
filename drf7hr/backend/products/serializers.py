from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    detailsUrl = serializers.SerializerMethodField(read_only=True)
    updateUrl = serializers.SerializerMethodField(read_only=True)
    detailsUrl = serializers.SerializerMethodField(read_only=True)
    detailsUrl2 = serializers.HyperlinkedIdentityField(   #notes:8
        view_name='product-detail',
        lookup_field='pk'
    )
    title = serializers.CharField(validators=[validate_title])
    class Meta:
        model = Product
        fields = [
            'detailsUrl',
            'detailsUrl2',
            'updateUrl',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
        
        
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs:
    #         raise serializers.ValidationError("This title already exists")
    #     return value
        
    def get_detailsUrl(self, instance):
        print(instance)
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-detail",  kwargs={"pk": instance.pk}, request=request)
    
    def get_updateUrl(self, instance):
        print(instance)
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-update", kwargs={"pk": instance.pk}, request=request)
                
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
    
class newSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'url',
            ]