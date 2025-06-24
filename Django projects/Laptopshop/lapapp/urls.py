from django.urls import path, include
from rest_framework import routers
from .views import Category_ViewSet, Sub_Category_ViewSet, Product_ViewSet, Branch_ViewSet

router = routers.DefaultRouter()
router.register(r'category', Category_ViewSet)
router.register(r'sub_category', Sub_Category_ViewSet)
router.register(r'product', Product_ViewSet)
router.register(r'branch', Branch_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
