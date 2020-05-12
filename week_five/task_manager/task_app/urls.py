from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tasks/new', views.new),
    path('tasks', views.tasks),
    path('tasks/create', views.create_task),
    path('task/<int:id>', views.one_task),
    path('edit/<int:id>', views.show_edit_page),
    path('update/<int:id>', views.process_edit),
    path('task/<int:id>/complete', views.delete_task)
]