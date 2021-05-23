from django.urls import path
from . import views

urlpatterns = [
    path('status', views.statusView, name='status'),
    path('', views.indexView, name='Home'),
    path('login', views.loginView, name="Login"),
    path('register', views.registerView, name="Register"),
]
