from django.urls import path, include
from rest_framework import routers

from .views import Category_Viewset, Test_Viewset

router = routers.DefaultRouter()
router.register(r'category', Category_Viewset)
router.register(r'test', Test_Viewset)


urlpatterns = [
    path('', include(router.urls))
]