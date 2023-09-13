from django.urls import path
from .views import PosterViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
]

router = DefaultRouter()
router.register('postes', PosterViewSet)  # 只包含五种默认的

urlpatterns += router.urls

