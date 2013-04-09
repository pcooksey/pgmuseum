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
		response = self.client.post("/accounts/", { 'signin': 'true', 'email': 'pcooksey@csumb.edu', 'password': 'secret'})
		self.assertEqual(response.status_code, 200)
		self.assertEquals(response.context['error'], 'Incorrect username or password!')
		response = self.client.post("/accounts/", { 'signin': 'true', 'password': 'secret'})
		self.assertEqual(response.status_code, 200)
		response = self.client.post("/accounts/", { 'signin': 'true', 'email': 'pcooksey@csumb.edu'})
		self.assertEqual(response.status_code, 200)
	
	def testRegister(self):
		response = self.client.post("/accounts/", { 'register': 'true'})
		#Redirect code is 302
		self.assertEqual(response.status_code, 302)
		response = self.client.post("/accounts/register/", {})
		self.assertEqual(response.status_code, 200)
		response = self.client.post("/accounts/register/", {'createAccount': 'true'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['error'], "Please enter information in every field!")
		response = self.client.post("/accounts/register/", {'createAccount': 'true', 'email': 'pcooksey@csumb.edu', 'password': 'password', 'confirmPassword': 'password', 'firstName': 'bob', 'lastName': 'smith'})
		self.assertEqual(response.status_code, 302)
		response = self.client.post("/accounts/register/", {'createAccount': 'true', 'email': 'pcooksey@csumb.edu', 'password': 'password', 'confirmPassword': 'password', 'firstName': 'bob', 'lastName': 'smith'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['error'], "User already exists!")
		response = self.client.post("/accounts/register/", {'createAccount': 'true', 'email': 'pcooksey1@csumb.edu', 'password': 'password', 'confirmPassword': 'password1', 'firstName': 'bob', 'lastName': 'smith'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['error'], "Your passwords do not match!")