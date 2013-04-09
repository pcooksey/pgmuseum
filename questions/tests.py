"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


class SimpleTest(TestCase):
	def setUp(self):
		self.client = Client()
		
	def testLogin(self):
		#Login with not vaild
		response = self.client.post("/accounts/", { 'signin': 'true', 'email': 'pcooksey@csumb.edu', 'password': 'secret'})
		self.assertEqual(response.status_code, 200)
		self.assertEquals(response.context['error'], 'Incorrect username or password!')
		#Login in with no information
		response = self.client.post("/accounts/", { 'signin': 'true'})
		self.assertEqual(response.status_code, 200)
		self.assertEquals(response.context['error'], 'Incorrect username or password!')
		#Login with only a password
		response = self.client.post("/accounts/", { 'signin': 'true', 'password': 'secret'})
		self.assertEqual(response.status_code, 200)
		self.assertEquals(response.context['error'], 'Incorrect username or password!')
		#Login with only email
		response = self.client.post("/accounts/", { 'signin': 'true', 'email': 'pcooksey@csumb.edu'})
		self.assertEqual(response.status_code, 200)
		self.assertEquals(response.context['error'], 'Incorrect username or password!')
	
	def testRegister(self):
		#Simple access to the register page (Redirect code is 302)
		response = self.client.post("/accounts/", { 'register': 'true'})
		self.assertEqual(response.status_code, 302)
		#Direct access to the register page
		response = self.client.post("/accounts/register/", {})
		self.assertEqual(response.status_code, 200)
		#Create account with no information
		response = self.client.post("/accounts/register/", {'createAccount': 'true'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['error'], "Please enter information in every field!")
		#Create a valid account
		response = self.client.post("/accounts/register/", {'createAccount': 'true', 'email': 'pcooksey@csumb.edu', 'password': 'password', 'confirmPassword': 'password', 'firstName': 'bob', 'lastName': 'smith'})
		self.assertEqual(response.status_code, 302)
		#Create the same account as before and error out
		response = self.client.post("/accounts/register/", {'createAccount': 'true', 'email': 'pcooksey@csumb.edu', 'password': 'password', 'confirmPassword': 'password', 'firstName': 'bob', 'lastName': 'smith'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['error'], "User already exists!")
		#Create new account with different passwords
		response = self.client.post("/accounts/register/", {'createAccount': 'true', 'email': 'pcooksey1@csumb.edu', 'password': 'password', 'confirmPassword': 'password1', 'firstName': 'bob', 'lastName': 'smith'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['error'], "Your passwords do not match!")
		#Create with empty passwords
		response = self.client.post("/accounts/register/", {'createAccount': 'true', 'email': 'pcooksey1@csumb.edu', 'password': '', 'confirmPassword': '', 'firstName': 'bob', 'lastName': 'smith'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['error'], "Please enter information in every field!")
		
		#Testing the login 
		response = self.client.post("/accounts/", { 'signin': 'true', 'email': 'pcooksey@csumb.edu', 'password': 'password'})
		self.assertEqual(response.status_code, 302)