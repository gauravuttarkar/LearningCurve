"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views
from django.urls import path, include
from login import urls as login_urls
from school import urls as school_urls
from volunteers import urls as volunteer_urls

urlpatterns = [
	
    path('admin/', admin.site.urls),
    path('authenticate/',include(login_urls)),
    path('school/',include(school_urls)),
    path('volunteers/',include(volunteer_urls)),
    path('',views.home),

]