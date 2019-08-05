from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter
from rest_framework import generics
from rest_framework import permissions

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
