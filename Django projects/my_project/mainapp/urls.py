from django.urls import path, include
from rest_framework import routers

from .views import Ceckin_Viewset


router = routers.DefaultRouter()
router.register(r'check_in', Ceckin_Viewset)

urlpatterns = [
    path('', include(router.urls))
]