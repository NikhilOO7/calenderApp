from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entry/<int:pk>/', views.details, name='details'),
]