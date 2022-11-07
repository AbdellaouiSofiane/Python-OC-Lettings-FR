from django.test.testcases import TestCase
from django.urls import reverse

from .models import Address, Letting
from .views import lettings_index, letting


class LettingBaseTest(TestCase):

    def setUp(self):
        address = Address.objects.create(
            number=57,
            street='somewhere',
            city='techland',
            state='NY',
            zip_code='95100',
            country_iso_code='USA',
        )
        self.letting = Letting.objects.create(title='test', address=address)


class LettingsIndexViewTest(LettingBaseTest):

    def setUp(self):
        super().setUp()
        self.response = self.client.get(reverse('lettings:lettings_index'))

    def test_template(self):
        self.assertTemplateUsed(self.response, 'lettings/index.html')

    def test_view(self):
        self.assertEqual(self.response.resolver_match.func, lettings_index)

    def test_title(self):
        self.assertIn('Lettings', str(self.response.content))

    def test_context(self):
        self.assertIn('lettings_list', self.response.context)
        self.assertIn(self.letting, self.response.context.get('lettings_list'))


class LettingViewTest(LettingBaseTest):

    def setUp(self):
        super().setUp()
        self.response = self.client.get(
            reverse('lettings:letting', args=[self.letting.id]))

    def test_template(self):
        self.assertTemplateUsed(self.response, 'lettings/letting.html')

    def test_view(self):
        self.assertEqual(self.response.resolver_match.func, letting)

    def test_title(self):
        self.assertIn(self.letting.title, str(self.response.content))

    def test_context(self):
        self.assertIn('title', self.response.context)
        self.assertIn('address', self.response.context)
        self.assertEqual(self.response.context.get('address'), self.letting.address)
