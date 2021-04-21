from django.test import SimpleTestCase
from budgetApp.forms import ExpenseForm


class TestForms(SimpleTestCase):

    def test_expense_form_valid_data(self):
        form = ExpenseForm(data={
            'title': 'expenseForm1',
            'amount': 5000,
            'category': 'design'
        })

        self.assertTrue(form.is_valid())

    def test_expense_form_no_data(self):
        form = ExpenseForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)