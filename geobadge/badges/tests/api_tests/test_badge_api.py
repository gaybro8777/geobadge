from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from geobadge.accounts.factories import UserFactory
from geobadge.badges.factories import BadgeFactory


class BadgeListApiTestCase(APITestCase):

    def setUp(self):
        super(BadgeListApiTestCase, self).setUp()

        self.user = UserFactory()
        self.user.set_password('test')
        self.user.save()

        self.endpoint = reverse('api:badge-list')

    def test_not_logged_in(self):
        """
        No authorization when the user is not logged in.
        """
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get(self):
        self.client.login(username=self.user.username, password='test')

        response = self.client.get(self.endpoint)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        self.client.login(username=self.user.username, password='test')

        data = {}

        response = self.client.post(
            self.endpoint,
            data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class BadgeDetailApiTestCase(APITestCase):

    def setUp(self):
        super(BadgeDetailApiTestCase, self).setUp()

        self.user = UserFactory()
        self.user.set_password('test')
        self.user.save()

        self.badge = BadgeFactory()
        self.endpoint = reverse('api:badge-detail', args=[self.badge.id])

    def test_not_logged_in(self):
        """
        No authorization when the user is not logged in.
        """
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get(self):
        self.client.login(username=self.user.username, password='test')

        response = self.client.get(self.endpoint)

        print(response)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch(self):
        self.client.login(username=self.user.username, password='test')

        data = {}

        response = self.client.patch(
            self.endpoint,
            data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        self.client.login(username=self.user.username, password='test')

        response = self.client.delete(self.endpoint)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
