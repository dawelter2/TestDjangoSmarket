from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_list),
    path("create_user/", views.create_user,),
    path("remove_user/<int:user_id>/", views.delete_user),
    path('user/<int:user_id>/', views.user_detail),
    path('user/<int:user_id>/create_task/', views.create_task),
    path('user/<int:user_id>/update_task/<int:task_id>/', views.update_task),
    path('user/<int:user_id>/remove_task/<int:task_id>/', views.delete_task),
]
