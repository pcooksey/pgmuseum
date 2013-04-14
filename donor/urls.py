from django.conf.urls import patterns, url
from donor import views

urlpatterns = patterns("", 
  url(r"^$", views.index, name="index"),
  url(r"^createNewDonor/", views.createNewDonor, name="createNewDonor"),
  url(r"^deleteDonor/", views.deleteDonor, name="deleteDonor"),
)
