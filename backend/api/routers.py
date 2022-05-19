from rest_framework import routers

from api import views as api_views
from api.user.viewsets import UserViewSet
from api.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet

user_router = routers.DefaultRouter()
user_router.register(r'auth/login', LoginViewSet, basename='auth-login')
user_router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
user_router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

user_router.register(r'user', UserViewSet, basename='user')

api_router = routers.DefaultRouter()
api_router.register(r'question', api_views.TranslationView, 'Translation')

urlpatterns = [
    *user_router.urls
]