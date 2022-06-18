from rest_framework import routers

from api import views as api_views

api_router = routers.DefaultRouter()
api_router.register(r'question', api_views.TranslationView, 'Translation')
