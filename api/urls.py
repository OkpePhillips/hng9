from django.urls import path

from .views import ListMyDetail

urlpatters = [
    path('', ListMyDetail.as_view()),
]