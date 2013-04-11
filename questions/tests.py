from django.test import TestCase
from django.test.client import Client

class SimpleTest(TestCase):
  def setUp(self):
    self.client = Client()
