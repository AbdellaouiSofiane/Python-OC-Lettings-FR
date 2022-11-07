from django.test.testcases import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Profile
from .views import profiles_index, profile


class ProfileBaseTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(username='test', password='1234')
        self.profile = Profile.objects.create(user=user, favorite_city='Techland')


class ProfilesIndexViewTest(ProfileBaseTest):

    def setUp(self):
        super().setUp()
        self.response = self.client.get(reverse('profiles:profiles_index'))

    def test_template(self):
        self.assertTemplateUsed(self.response, 'profiles/index.html')

    def test_view(self):
        self.assertEqual(self.response.resolver_match.func, profiles_index)

    def test_title(self):
        self.assertIn('Profiles', str(self.response.content))

    def test_context(self):
        self.assertIn('profiles_list', self.response.context)
        self.assertIn(self.profile, self.response.context.get('profiles_list'))


class ProfileViewTest(ProfileBaseTest):

    def setUp(self):
        super().setUp()
        self.response = self.client.get(
            reverse('profiles:profile', args=[self.profile.user.username]))

    def test_template(self):
        self.assertTemplateUsed(self.response, 'profiles/profile.html')

    def test_view(self):
        self.assertEqual(self.response.resolver_match.func, profile)

    def test_title(self):
        self.assertIn(self.profile.user.username, str(self.response.content))

    def test_context(self):
        self.assertIn('profile', self.response.context)
        self.assertEqual(self.response.context.get('profile'), self.profile)
