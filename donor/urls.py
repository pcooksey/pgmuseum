from django.conf.urls import patterns, url
from donor import views

urlpatterns = patterns("", 
  url(r"^$", views.index, name="index"),
  url(r"^createNewDonor/", views.createNewDonor, name="createNewDonor"),
  url(r"^deleteDonor/", views.deleteDonor, name="deleteDonor"),
  url(r"^donations/", views.donations, name="donations"),
  url(r"^createNewDonation/", views.createNewDonation, name="createNewDonation"),
  url(r"^deleteDonation/", views.deleteDonation, name="deleteDonation"),
)
