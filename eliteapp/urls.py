from django.urls import path 
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loggedin, name='login'),
    path('', views.home, name="home"),
    path('logout/', views.loggedout, name='logout'),
    path('add-post/', views.add_post, name='add-post'),
]