from products.viewsets import ProductViewSet, ProductGenericViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"products-abc", ProductGenericViewSet , basename="hakuna_matata")
print(router.urls)
urlpatterns = router.urls