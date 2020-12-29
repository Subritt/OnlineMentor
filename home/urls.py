from django.contrib import admin
from django.urls import path, include
from home import views
# Django admin Header Custumization


urlpatterns = [

    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('tutor', views.tutor, name='tutor'),
    path('contactus', views.contactus, name='contactus'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('blog', views.blog, name='blog')


]
