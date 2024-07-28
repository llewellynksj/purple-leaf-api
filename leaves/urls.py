from django.urls import path
from leaves import views

urlpatterns = [
  path('leaves/', views.LeafList.as_view()),
  path('leaves/<int:pk>/', views.LeafDetail.as_view()),
]