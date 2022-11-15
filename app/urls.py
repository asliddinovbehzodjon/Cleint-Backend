from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('',BotUserViewset)
urlpatterns = [
    path('create',include(router.urls)),
     path('status/',TimeInfo.as_view()),
]
