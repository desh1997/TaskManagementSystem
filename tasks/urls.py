from django.urls import path
from .views import RegisterView, TaskViewSet, LoginView

from rest_framework import routers

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns += router.urls
