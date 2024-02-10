from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('signin/', views.LoginView.as_view(), name='signin'),
    path('signout/', views.signout, name='signout'),
    path('recipe/', views.create_recipe, name='recipe'),
]
