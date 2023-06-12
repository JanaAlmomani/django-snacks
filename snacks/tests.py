from django.test import TestCase,SimpleTestCase
from django.urls import reverse

# Create your tests here.
class MyProjectTestCase(TestCase):
    def test_home_url_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_url_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_home_url_template_use(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'home.html')

    def test_about_url_template_use(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')
       