from django.conf.urls import patterns, url
from datasheet import views

urlpatterns = patterns("", 
  url(r"^$", views.index, name="index"),
  url(r"^next/$", views.next, name="next"),
  url(r"^next/flowers", views.flowers, name="flowers"),
  url(r"^delete/$", views.next, name="delete"),
)
