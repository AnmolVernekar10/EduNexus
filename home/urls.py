"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [    
    #path('',views.index,name='home'),
    # path('/test',views.test,name='test'),post_signin
    path('signin',views.signin,name='signin'),
    path('main_page/',views.main_page,name='main_page'),
    path('home_page/',views.home_page,name='home_page'),
    path('logout/',views.logout,name='log'),
    path('signup/',views.signup,name='signup'),
    path('searchfile/',views.searchfile,name='searchfile'),
    path('postsignup/',views.postsignup,name='postsignup'),
    path('postsignin/',views.postsignin,name='postsignin'),
    path('post_signin/',views.postsignin,name='postsignin'),
    path('search/',views.searchTest,name='searchTest'),
    path('clear/',views.clear,name='clear'),
    path('searchBar/',views.searchBar,name='searchBar'),
    path('test/',views.modalTest,name='modalTest'),
    path('readmore/',views.readmore,name='readmore'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)