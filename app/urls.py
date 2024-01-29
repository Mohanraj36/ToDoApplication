from django.urls import path
from . import views
urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', views.TaskDelete.as_view(), name='task-delete'),
    path('task-reorder/', views.TaskReorder.as_view(), name='task-reorder'),
]
