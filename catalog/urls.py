from django.urls import path, include
from .views import IndexView

from rest_framework import routers
from .api.viewsets import AuthorViewSet, BookViewSet
router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/', include(router.urls)),
]
