from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns("", 
  url(r"^$", views.index, name="index"),
  url(r"^register/$", views.register, name="register"),
  url(r"^home/$", views.home, name="home"),
  url(r"^logout/$", views.logoutPage, name="logout"),
)
