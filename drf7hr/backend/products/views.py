from rest_framework import generics, mixins, permissions, viewsets

from .models import Product
from .serializers import ProductSerializer, newSerializer
from api.permissions import IsStaffEditorPermission
from api.mixins import StaffEditorPermissionMixin


class ProductListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()  # notes:6
    serializer_class = newSerializer
    permission_classes = []


    def perform_create(self, serializer):
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "perform create is used to customise the create method, as we can see, if the content is not provided, it will be set to this default value."
        serializer.save(content=content)


class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()  # notes:3,4,5
    serializer_class = ProductSerializer
    permission_classes = []
    # lookup_field = "pk"  this is the default field


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


    def perform_update(self, serializer):  # for more custom things
        instance = serializer.save()
        # if instance.price < 10000:
        #     instance.price = 99999
        #     instance.save()
        if not instance.content:
            instance.content = "perform update is used to customise the update method, as we can see, if the content is not provided, it will be set to this default value."
            instance.save()


class ProductDeleteAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    #this permission_class is used to override the default permission classes if required.


    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


def using_mixins_below(this_function_has_no_purpose):

    # #mixins
    # class ProductMixinAPIView(mixins.ListModelMixin,
    #                           mixins.CreateModelMixin,
    #                           mixins.RetrieveModelMixin,
    #                           mixins.UpdateModelMixin,
    #                           mixins.DestroyModelMixin,
    #                           generics.GenericAPIView):
    #     queryset = Product.objects.all()
    #     serializer_class = ProductSerializer
    #     lookup_field = "pk"

    #     def get(self, request,*args, **kwargs):
    #         pk = kwargs.get("pk")
    #         print(pk)
    #         if pk is not None:
    #             return self.retrieve(request, *args, **kwargs)
    #         return self.list(request, *args, **kwargs)

    #     def post(self, request, *args, **kwargs):
    #         return self.create(request, *args, **kwargs)

    #     def put(self, request, *args, **kwargs):
    #         return super().update(request, *args, **kwargs)

    #     def delete(self, request, *args, **kwargs):
    #         return self.destroy(request, *args, **kwargs)

    #         # methods like perform_create, perform_update, perform_destroy can be works here as well, as it extends to generics.GenericAPIView etc
    pass



