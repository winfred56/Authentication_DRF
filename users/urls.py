from django.urls import path
from . import views

urlpatterns =[
    path('', views.UsersList.as_view(), name='users_list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/blacklist/', views.BlacklistTokenUpdateView.as_view(), name='blacklist'),
]