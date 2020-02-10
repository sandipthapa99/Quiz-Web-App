from django.test import TestCase
from .forms import ResourceForm

# Create your tests here.

class TestForms(TestCase):

	def test_resource_form(self):
		form = ResourceForm(data={
				'title': 'Test',
				'author': 'admin',
			})

		self.assertFalse(form.is_valid())

	def test_resource_form_no_data(self):
		form = ResourceForm(data={})

		self.assertFalse(form.is_valid())