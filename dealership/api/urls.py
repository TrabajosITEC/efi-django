from rest_framework.routers import DefaultRouter, path
from api.views.cars_views import CarViewSet
from api.views.register_views import UserRegisterViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet,'cars')
router.register(r'register', UserRegisterViewSet, 'register')

urlpatterns = [

]

urlpatterns += router.urls