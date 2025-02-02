# profiles/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet
from . import views

# A router segít az API végpontok kezelésében
router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)  # A 'profiles' végpont regisztrálása a ProfileViewSet-tel

urlpatterns = router.urls  # A router által generált URL-ek
