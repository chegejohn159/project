"""KaGeo URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from GeoKa.views import signup,movie,main,index

from django.contrib import admin
from django.urls import include
from django.contrib.auth import views

#from django.contrib.auth import views as auth_views



urlpatterns = [
	path('',index),

    path('signup/',signup),
    path('cat/',main),
    #path('login/',login),
    path('page/',movie),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]

   # path('login/','django.contrib.auth.views.LoginView', {'template_name': '/login.html'}),
    #path('login/','django.contrib.auth.views.login'),
    #path('login/', auth_views.LoginView, name='login'),
    # path('logout/', auth_views.LogoutView, name='logout'),
    # path('admin/', admin.site.urls),
    

