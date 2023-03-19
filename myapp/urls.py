from django.urls import path,include 
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('students',StudentViewSet)
router.register('subjects',SubjectViewSet)
router.register('groups',GroupViewSet)
urlpatterns = [
    path('',include(router.urls))
]
