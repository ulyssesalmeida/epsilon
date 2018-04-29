from django.test import TestCase

# Create your tests here.

class pipTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/projetos/')

    def test_get(self):
        'GET /projetos/ must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template'
        self.assertTemplateUsed(self.resp, 'projects/pip_form.html')

    def test_html(self):
        'HTML must contain some input controls'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input',19)
        self.assertContains(self.resp, 'type="test"',4)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'HTML must contain csrf django token'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context must have pip form'
        form = self.resp.context['form']
        self.assertIsInstance(form, PipForm)

    def test_form_has_fields(self):
        'PIP form must have some fields'
        form = self.resp.context['form']
        self.assertItemsEqual(['title','orgUnit','client','justification','objectives','cost_estimates'], form.fields)
