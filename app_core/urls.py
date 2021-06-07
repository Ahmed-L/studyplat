from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home.html'),
    path('home', views.home, name='home.html'),
    # path('subject', views.subject, name='subject_page.html'),
    # path('chapter', views.chapter, name='chapter.html')
]
