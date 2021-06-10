"""study_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from app_core.views import subject, chapter, home, search
from quiz.views import quiz_view

urlpatterns = [
    path('', home, name='app_core/home.html'),
    path('main/', include('app_core.urls')),
    path('home', home, name='home'),
    path('admin/', admin.site.urls),
    path('subject/<str:name>', subject, name='subject'),
    path('chapter/<str:name>', chapter, name='chapter'),
    path('search', search, name='search'),
    path('quiz/<str:name>', quiz_view, name='quiz')
    # path('subject', subject, name='subject'),
    # path('chapter', chapter, name='chapter')
]