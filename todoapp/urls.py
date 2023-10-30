from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.add, name='add'),
    path('details/', views.details, name='details'),
    path('delete/<int:taskid>', views.delete, name='delete'),
    path('update/<int:taskid>', views.update, name='update'),

    path('chome', views.TaskList.as_view(), name='chome'),
    path('cdetail/<int:pk>/', views.TaskDetail.as_view(), name='cdetail'),
    path('cupdate/<int:pk>/', views.TaskUpdate.as_view(), name='cupdate'),
    path('cadd', views.TaskCreate.as_view(), name='cadd'),
    path('cdelete/<int:pk>/', views.TaskDelete.as_view(), name='cdelete'),

]
