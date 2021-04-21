from django.test import TestCase
from budgetApp.models import Project, Expense, Category


class TestModels(TestCase):

    def setUp(self):
        self.projectTest = Project.objects.create(name='TestProject', budget=5000)

    def test_project_is_assigned_slug_on_creation(self):
        self.assertEqual(self.projectTest.slug, 'testproject')

    def test_budget_left(self):
        category = Category.objects.create(project=self.projectTest, name='design')

        Expense.objects.create(project=self.projectTest, title='expense1', amount=1000, category=category)
        Expense.objects.create(project=self.projectTest, title='expense2', amount=3000, category=category)

        self.assertEqual(self.projectTest.budget_left, 1000)

    def test_total_transaction(self):
        project0 = Project.objects.create(name='project0', budget=5000)
        category = Category.objects.create(project=project0, name='design')

        Expense.objects.create(project=project0, title='expense1', amount=1000, category=category)
        Expense.objects.create(project=project0, title='expense2', amount=3000, category=category)

        self.assertEqual(project0.total_transactions, 2)