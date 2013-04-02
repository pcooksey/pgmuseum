from django.conf.urls import patterns, url
from questions import views

urlpatterns = patterns("", 
  url(r'^$', views.index, name="index"),
  url(r'^inputs/', views.inputs, name="inputs")
)
