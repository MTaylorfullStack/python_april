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
    path('like/<int:mess_id>', views.add_like),
    path('profile/<int:user_id>', views.profile),
    path('edit/<int:user_id>', views.edit_user),
    path('delete/<int:mess_id>', views.destroy_mess),
    path('edit_mess/<int:mess_id>', views.edit_mess)
]


