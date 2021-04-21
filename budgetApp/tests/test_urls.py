from django.test import SimpleTestCase
from django.urls import resolve, reverse
from budgetApp.views import project_list, project_detail, ProjectCreateView


class TestUrls(SimpleTestCase):

    def test_list_url_resolved(self):
        url = reverse('list')
        self.assertEqual(resolve(url).func, project_list)

    def test_add_url_resolve(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func.__name__, ProjectCreateView.__name__)

    def test_detail_url_resolve(self):
        url = reverse('detail', args=['test-project'])
        self.assertEqual(resolve(url).func, project_detail)
