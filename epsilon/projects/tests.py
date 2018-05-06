from django.test import TestCase
from django.db import IntegrityError
from epsilon.projects.forms import PipForm
from epsilon.projects.models import Pip
from datetime import date

# Create your tests here.

class pipViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/projetos/pip/')

    def test_get(self):
        'GET /projetos/pip must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template'
        self.assertTemplateUsed(self.resp, 'projects/pip_form.html')

    def test_html(self):
        'HTML must contain some input controls'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input',6)
        self.assertContains(self.resp, '<textarea',2)
        self.assertContains(self.resp, 'type="text"',4)
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
        self.assertListEqual(['title','orgUnit','client','justification','objectives','cost_estimates'], [x for x in form.fields])

class pipPostTest(TestCase):
    def setUp(self):
        data = dict(
            title = 'Epsilon',
            orgUnit = 'EPSTI',
            client = 'EPSTI',
            justification = 'Necessidade de sistema automatizado para auxiliar no gerenciamento de portfolio do EPSTI',
            objectives = 'Criar um sistema WEB para facilitar a gerencia de projetos e porfolios seguindo a metodologia adotada pelo EPSTI',
            cost_estimates = 'diarias;suprimento_de_fundos;usts',
            )
        self.resp = self.client.post('/projetos/pip/')

    def test_post(self):
        'Valid POST must redirect to /projetos/pip/P<year><id>/'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        'PIP must exist after saving!'
        self.assertTrue(Pip.objects.exists())

class pipModelTest(TestCase):
    def setUp(self):
        self.current_year = date.today().year
        self.obj = Pip(
            title = 'Epsilon',
            orgUnit = 'EPSTI',
            client = 'EPSTI',
            justification = 'Necessidade de sistema automatizado para auxiliar no gerenciamento de portfolio do EPSTI',
            objectives = 'Criar um sistema WEB para facilitar a gerencia de projetos e porfolios seguindo a metodologia adotada pelo EPSTI',
            cost_estimates = 'diarias;suprimento_de_fundos;usts',
            )

    def test_create(self):
        'PIP must have title, orgUnit, justification, objectives'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_proposal_year_based_id(self):
        'PIP must have one proposal id based on the current year'
        self.obj.save()
        self.assertEqual(self.obj.pipId, 'P{}{:03d}'.format(self.current_year,1))

    def test_proposal_unique_id(self):
        'PIP id must be unique and incremental'
        pip = Pip(
            title = 'Epsilon2',
            orgUnit = 'GABSTI',
            client = 'Servidores',
            justification = 'Apenas mais um projeto com nome repedito',
            objectives = 'Verificar se o sistema impede criacao do segundo PIP com mesmo titulo',
            cost_estimates = '',
            )
        self.obj.save()
        pip.save()
        self.assertEqual(pip.pipId, 'P{}{:03d}'.format(self.current_year,2))

    def test_unique_title(self):
        'Pip title must be unique to avoid confusion within portfolio'
        pip = Pip(
            title = 'Epsilon',
            orgUnit = 'GABSTI',
            client = 'Servidores',
            justification = 'Apenas mais um projeto com nome repedito',
            objectives = 'Verificar se o sistema impede criacao do segundo PIP com mesmo titulo',
            cost_estimates = '',
            )
        self.obj.save()
        self.assertRaises(IntegrityError, pip.save)

    def test_update_proposal(self):
        'While changing PIP, pipId must remain the same'
        self.obj.save()
        self.obj.title = "Epsilon updated"
        self.obj.save()
        self.assertEqual(self.obj.pipId, 'P{}{:03d}'.format(self.current_year,1))
