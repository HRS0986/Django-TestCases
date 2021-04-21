from django.test import TestCase, Client
from django.urls import reverse
from budgetApp.models import Project, Expense, Category
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['project-test'])
        self.project_test = Project.objects.create(name='project-test', budget=1000)

    def test_project_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-list.html')

    def test_project_details_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-detail.html')

    def test_project_detail_POST_add_new_expense(self):
        cat_design = Category.objects.create(project=self.project_test, name='design')

        response = self.client.post(self.detail_url, {
            'title': 'expense0',
            'amount': 500,
            'category': 'design'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.project_test.expenses.first().title, 'expense0')
        self.assertEqual(self.project_test.expenses.first().amount, 500)
        self.assertEqual(self.project_test.expenses.first().category.name, 'design')

    def test_project_detail_POST_no_data(self):
        response = self.client.post(self.detail_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.project_test.expenses.count(), 0)

    def test_project_detail_DELETE_delete_expense(self):
        cat_qa = Category.objects.create(project=self.project_test, name='qa')
        Expense.objects.create(
            project=self.project_test,
            title='expense1',
            amount=200,
            category=cat_qa
        )
        self.assertEqual(self.project_test.expenses.count(), 1)
        response = self.client.delete(self.detail_url, json.dumps({'id': 1}))

        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.project_test.expenses.count(), 0)

    def test_project_detail_DELETE_no_id(self):
        cat_qa = Category.objects.create(project=self.project_test, name='qa')

        Expense.objects.create(
            project=self.project_test,
            title='expense1',
            amount=200,
            category=cat_qa
        )
        self.assertEqual(self.project_test.expenses.count(), 1)
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(self.project_test.expenses.count(), 1)

    def test_project_create_POST(self):
        url = reverse('add')
        response = self.client.post(url, {
            'name': 'project99',
            'budget': 40000,
            'categoriesString': 'dev,qa'
        })

        project99 = Project.objects.get(id=2)
        self.assertEqual(project99.name, 'project99')

        cat_design = Category.objects.get(id=1)
        cat_qa = Category.objects.get(id=2)

        self.assertEqual(cat_design.name, 'dev')
        self.assertEqual(cat_qa.name, 'qa')
        self.assertEqual(cat_design.project, project99)
        self.assertEqual(cat_qa.project, project99)

