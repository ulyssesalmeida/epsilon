from django.test import TestCase

# Create your tests here.
class MainPageTest(TestCase):
    def test_get(self):
        'GET deve retornar codigo de status 200'
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'index.html')