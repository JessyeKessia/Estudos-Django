from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, EditoraViewSet

router = DefaultRouter()

router.register(r'autores', AutorViewSet)
router.register(r'editoras', EditoraViewSet)

urlpatterns = router.urls