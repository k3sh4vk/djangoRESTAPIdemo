"""djangoREST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views as restapiView

urlpatterns = [
    path('', restapiView.apiAccess, name='apiAccess'),
    path('register*', restapiView.loginView, name='loginView'),
    path('user-list/', restapiView.userList, name='user-list'),
    path('user-detail/<int:pk>/', restapiView.userDetail, name='user-detail'),
    path('user-create/', restapiView.userCreate, name='user-create'),
    path('user-update/<int:pk>/', restapiView.userUpdate, name='user-update'),
    path('user-delete/<int:pk>/', restapiView.userDelete, name='user-delete'),
]
