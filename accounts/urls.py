from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns("", 
  url(r"^$", views.index, name="index"),
  url(r"^register/$", views.register, name="register"),
  url(r"^home/$", views.home, name="home"),
  url(r"^logout/$", views.logoutPage, name="logout"),
  url(r"^home/export/$", views.export, name="export"),
  url(r"^home/data/$", views.extraInformation, name="data"),
  url(r"^home/delete/$", views.next, name="delete"),
)
