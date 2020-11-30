from rest_framework.routers import DefaultRouter
from apps.departmants.views import DepartmentAPIViewSet


router = DefaultRouter()
router.register(r'', DepartmentAPIViewSet, basename='departments')

urlpatterns = router.urls
