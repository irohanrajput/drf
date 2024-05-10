from django.urls import path
from . import views
from . import viewsets

urlpatterns = [
    path("<int:pk>/", views.ProductDetailAPIView.as_view(), name="product-detail"),
    path("<int:pk>/update", views.ProductUpdateAPIView.as_view(), name="product-update"),
    path("<int:pk>/delete", views.ProductDeleteAPIView.as_view(), name="product-delete"),
    path("", views.ProductListCreateAPIView.as_view(), name="product-list"),
    
    
    
    path("using_viewsets/", viewsets.product_list_view, name="product-list-viewset"),
    # path("", views.ProductMixinAPIView.as_view(), name="product_list"),
    # path("<int:pk>/", views.ProductMixinAPIView.as_view(), name="product_detail"),
    # path("<int:pk>/update", views.ProductMixinAPIView.as_view(), name="product_update"),
    # path("<int:pk>/delete", views.ProductMixinAPIView.as_view(), name="product_delete")
]
