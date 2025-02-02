from django.urls import path
from .views import ProfileListCreateView

urlpatterns = [
    path('', ProfileListCreateView.as_view(), name='profile-list'),
]
