from rest_framework import routers

from api.user.viewsets import UserViewsets
from api import views as api_views


user_router = routers.DefaultRouter()
user_router.register('user', UserViewsets, basename='user_api')

api_router = routers.DefaultRouter()
api_router.register(r'question', api_views.TranslationView, 'Translation')