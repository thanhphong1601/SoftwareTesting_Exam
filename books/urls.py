from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', views.BookAPIViewSet, basename='books')
router.register('customers', views.CustomerAPIView, basename='customers')

urlpatterns = [
    path('', include(router.urls))
]
