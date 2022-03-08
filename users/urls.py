from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns =[
    path('', views.UsersList.as_view(), name='users_list'),
    path('register/', views.RegisterView.as_view(), name='register'),
]