from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.create_user),
    path('feed', views.feed),
    path('create_message', views.create_message),
    path('likes/<int:id>', views.like_message)
]
