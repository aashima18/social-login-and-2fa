from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from .import views
from .views import *
urlpatterns = [
   path('',views.indexx,name='indexx'),
   path('index',views.index,name='index'),
   path('signup',views.signup,name='signup'),
   # path('login1/',views.user_login,name='login1'),
   path('startt/',views.start_quiz,name='startt'),
   path('questions/',views.question_view,name='questions'),
   # path('logout',views.logout,name='logout'),
   path('answers/',views.submit_quiz,name='answers'),
   path('error/',views.error,name='error'),
   path('check_answer/<int:student_id>',views.check_answer,name='check_answers'),
   url(r'^oauth/', include('social_django.urls', namespace='social')),
]