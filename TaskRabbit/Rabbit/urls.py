from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('login/', views.login, name="login"),
    path('home/', views.home, name="home"),
    path('upload_image/', views.upload_image, name='upload_image')
]