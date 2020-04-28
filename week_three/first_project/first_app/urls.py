from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('goodbye', views.goodbye),
    path('<str:name>', views.name)
]
