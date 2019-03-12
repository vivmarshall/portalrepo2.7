from django.conf.urls import url, include
#from django.urls import path, include
from portal import views 
urlpatterns = [ 
     url(r'^$', views.HomePageView.as_view()),
     url('login/', views.login.as_view(),name='log_in'), 
     url('registration/', views.reg.as_view(),name='reg'),
     url('register/', views.register, name='register'),
     url('Welcome/',views.logging, name='logging') 
 ] 
