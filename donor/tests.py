from django.test import TestCase
from django.test.client import Client

class SimpleTest(TestCase):
  def setUp(self):
    self.client = Client()
   
  def testAddDonor(self):
    # Redirect to accounts
    response = self.client.post("/donor/", {})
    self.assertEqual(response.status_code, 302)
    response = self.client.post("/donor/createNewDonor/", { 'id_firstName': '', 'id_lastName': '', 'id_email': ''})
    self.assertEqual(response.status_code, 302)
    # Create user and login
    response = self.client.post("/accounts/register/", {'createAccount': 'true', 'email': 'student@csumb.edu', 'password': 'password', 'confirmPassword': 'password', 'firstName': 'bob', 'lastName': 'smith'})
    self.assertEqual(response.status_code, 302)
    response = self.client.post("/accounts/", { 'signin': 'true', 'email': 'pcooksey@csumb.edu', 'password': 'password'})

    # Now test adding a donor
    response = self.client.post("/donor/createNewDonor/", { 'id_firstName': '', 'id_lastName': '', 'id_email': ''})
    self.assertEqual(response.status_code, 302)
    self.assertEquals(self.client.session['error'], 'Your input was invalid')
    response = self.client.post("/donor/createNewDonor/", { 'id_firstName': 'bob', 'id_lastName': '', 'id_email': 'email@email.com'})
    self.assertEqual(response.status_code, 302)
    self.assertEquals(self.client.session['error'], 'Your input was invalid')
    response = self.client.post("/donor/createNewDonor/", { 'id_firstName': '', 'id_lastName': 'smith', 'id_email': 'email@email.com'})
    self.assertEqual(response.status_code, 302)
    self.assertEquals(self.client.session['error'], 'Your input was invalid')
    response = self.client.post("/donor/createNewDonor/", { 'id_firstName': 'bob', 'id_lastName': 'smith', 'id_email': ''})
    self.assertEqual(response.status_code, 302)
    self.assertEquals(self.client.session['error'], 'Your input was invalid')
    # Successfully add a Donor
    response = self.client.post("/donor/createNewDonor/", { 'id_firstName': 'bob', 'id_lastName': 'smith', 'id_email': 'bsmith@email.com'})
    self.assertEqual(response.status_code, 302)

  def testRemoveDonor(self):
    response = self.client.post("/donor/createNewDonor/", { 'id_firstName': '', 'id_lastName': '', 'id_email': ''})
    self.assertEqual(response.status_code, 302)
