from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/take/', views.exam_take, name='exam_take'),
    path('<slug:slug>/result/', views.exam_result, name='exam_result'),
]
