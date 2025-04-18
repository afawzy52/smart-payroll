"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views


urlpatterns = [
    #--------company urls
    path('settings/blank/',views.blank_view, name='blank'),
    path('settings/company/', views.comapny_update_view, name='company'),
    
    #--------branch urls
    path('settings/branch/', views.branch_list_view, name='branch-list'),
    path('settings/branch/add/', views.branch_add_view, name='branch_add'),
    
    # path('branch/<int:pk>/edit/', views.AuthorUpdate.as_view(), name='author-update'),
    path('settings/branch/<int:pk>/delete/', views.branch_delete_view, name='branch_delete'),
    #---------department urls
    path('settings/dept/', views.dept_list_view, name='dept-list'),
]