from django.test import TestCase

# Create your tests here.
class MainPageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        'GET deve retornar codigo de status 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Página inicial deve usar template index.html'
        self.assertTemplateUsed(self.resp, 'index.html')
