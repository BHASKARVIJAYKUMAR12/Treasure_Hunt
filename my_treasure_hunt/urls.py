"""
URL configuration for my_treasure_hunt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from members import views
urlpatterns = [
   # path('',include('members.urls')),
    path('admin/', admin.site.urls),
    path('',views.HomePage,name='home'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
 #   path('landingpage/',views.LandingPage,name='landingpage'),
    path('stage1/',views.Stage1,name='stage1'),
    path('stage2/',views.Stage2,name='stage2'),
    path('stage3/',views.Stage3,name='stage3'),
    path('stage4/',views.Stage4,name='stage4'),
    path('stage5/',views.Stage5,name='stage5'),
    path('profile/',views.Profile,name='profile'),
    path('logout/',views.Logout,name='logout'),
    path('contact/',views.Contact,name='contact'),
    path('treasure/',views.Treasure,name='treasure'),

        #  path('stage/<int:stage_id>/', views.stage, name='stage'),
  #  path('submit-answer/', views.submit_answer, name='submit_answer'),
]
