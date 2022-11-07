from django.test.testcases import TestCase
from django.urls import reverse

from .views import index


class IndexViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('index'))

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_view(self):
        self.assertEqual(self.response.resolver_match.func, index)

    def test_title(self):
        self.assertIn('Holiday Homes', str(self.response.content))
