from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('register/', views.register, name='register'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('reset_password/<str:email>/', views.reset_password, name='reset_password'),
    path('upload/', views.upload_image, name='upload_image'),
    # path('result/', views.result, name='result'),
]