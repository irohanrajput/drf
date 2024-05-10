from products.viewsets import ProductViewSet, ProductGenericViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"products-abc", ProductGenericViewSet , basename="hakuna_matata")
urlpatterns = router.urls