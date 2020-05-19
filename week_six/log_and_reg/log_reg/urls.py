from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('create_mess', views.create_mess),
    path('create_comm/<int:mess_id>', views.add_comm),
    path('like/<int:mess_id>', views.add_like)
]


