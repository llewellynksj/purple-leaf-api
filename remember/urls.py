from django.urls import path
from remember import views

urlpatterns = [
    path('remember/', views.RememberList.as_view()),
    path('remember/<int:pk>/', views.RememberDetail.as_view()),
]